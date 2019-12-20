[![python](https://img.shields.io/badge/Python-2.7--3.6-green.svg?style=style=flat-square)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-3.141.0-lightgrey.svg)](https://pypi.org/project/selenium/)
[![Beautiful Soup](https://img.shields.io/badge/BeautifulSoup-4.4.0-yellow.svg)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
# Facebook-Automation

>It automates Facebook login process by opening an instance of the native browser(in this case:Firefox) and enables the user to post status update.
>In the background it also scrapes some 'recent posts' , 'recent message's url' and 'Active friends'.
>It is only for Testing purposes

Platform : Linux 64 bit

Browser : Firefox by Mozilla

# Commands to setup Libraries
```sh
apt install python-pip

pip install -r setup.py

mv geckodriver /usr/bin/
```
# Libraries Used
| Library | README |
| ------ | ------ |
| Selenium | http://selenium-python.readthedocs.io/ |
| BeautifulSoup4 | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ |

-------------------------------------------------------------------------
* [Web Driver] - Firefox Web Driver Link

>Some modification and changes will be updated!!

>Continuously running the script may result into logout of your account from "Logged in devices"

[//]: #
[Web Driver]: <https://github.com/mozilla/geckodriver/releases>
