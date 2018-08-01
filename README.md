# Facebook-Automation

It automates Facebook login process by opening an instance of the native browser(in this case:Firefox) and enables the user to post status update.
In the background it also scrapes some 'recent posts' and 'recent message's url'.
It is only for Testing purposes

Platform : Linux 64 bit

Browser : Firefox by Mozilla

# Commands to setup Libraries
```sh
apt install python-pip

pip install -r setup.py

mv geckodriver /usr/bin/
```
# Libraries Used

Selenium --- http://selenium-python.readthedocs.io/
-------------------------------------------------------------------------
BeautifulSoup4 --- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
--------------------------------------------------------------------------
Link for Firefox WebDriver ----- https://github.com/mozilla/geckodriver/releases

Some modification and changes will be updated!!

Continuously running the script may result into logout of your account from "Logged in devices"
