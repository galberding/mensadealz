#!/set/path/to/interpreter
import requests
from bs4 import BeautifulSoup
import re
from sty import fg, bg, ef, rs, RgbFg

def printMenu(menu):
    title = fg.green + ef.u + ef.bold + menu[0] + rs.bold_dim + rs.u + fg.rs
    price = fg.red + menu[-1] + fg.rs
    separator = fg.da_yellow + 60 * "-" + fg.rs
    print(title)
    for i in menu[1:-1]:
        print(i)
    print(price)
    print(separator)


def get_page_menu(url):
    """GETs the page of the Stadtwerke Bielefeld and extracts the menus out of it."""
    thepage = requests.get(url)

    soup = BeautifulSoup(thepage.content, "html.parser")
    textfind = soup.find('div', {"class": "result"})
    menus = (textfind.contents[1])
    rows = ((menus.findAll("tr")))
    all_menu = {}
    count1 = 0
    for i in rows:
        count1 += 1
        menu = (i.find('td', {"class": "first"}))
        price = (i.find('td', {"width": "150px"}))
        if price is None:
            continue
        if price.string is None:
            continue
        price = price.string.replace("\n", "")

        if count1 == 7:
            break
        build_menu = []

        for j in menu.strings:
            if j is not None and len(j) > 4:
                j = re.sub('\s+', ' ', j).strip()
                build_menu.append(j)
        del build_menu[-1]
        build_menu.append(re.sub('\s+', ' ', price).strip())
        all_menu[build_menu[0]] = build_menu[1:]

        printMenu(build_menu)

    return all_menu


if __name__ == '__main__':

    url = "http://www.studierendenwerk-bielefeld.de/"
    menus = get_page_menu(url)
