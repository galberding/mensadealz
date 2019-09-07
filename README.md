# mensadealz
Simple python script for printing the mensa menu on terminal.
It will scrape the site http://www.studierendenwerk-bielefeld.de/ and basically print
the listed menus on the terminal in a readable format.

# Setup
To get this script running you need ```python3``` interpreter.

* Install the following packages:
```
pip install requests bs4 sty
```
 * Execute the script
 ```
python mensa.py
 ```
* For simply calling the script set a python interpreter in the first line
```python
#!/set/path/to/interpreter
import requests
from bs4 import BeautifulSoup
import re
[...]
```
* Export the path to call the script from everywhere. Add in your ```.bashrc```
```bash
export PATH=$PATH:/path/to/script/
```
* Start reading from the first line.
```bash
alias mensadealz='mensa.py | more'
```

# Limitations
* The script will only show menus of the current day, thus there will be no output on weekends