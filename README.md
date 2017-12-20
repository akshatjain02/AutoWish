# AutoWish
AutoWish is an automation script which wishes all your facebook friends who have their birthday today by posting 'Happy birthday' (customizable) on their facebook walls.

It uses Selenium Webdriver to create a browser object and login to your facebook ID after you enter your login credentials as input when prompted for.

The script runs on python3

### Install requirements
Selenium:
```
pip install selenium
```
Chrome WebDriver: [Install](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Notes
1. When creating a browser instance for the Chrome WebDriver in the code, set the path argument as the location of the chromedriver executable file.
2. The password input may be echoed. Be careful while testing the script in presence of other people.
3. If you want to test the script on Sublime Text Editor, which does not support console inputs in a build, then you can use [SublimeREPL](https://github.com/wuub/SublimeREPL) by following this [link](https://stackoverflow.com/questions/10604409/sublime-text-2-console-input).
4. Enter your FB username and password (echoed) as console input when asked.

### Bugs/TODOs
- [ ] Make the password input unechoed.
- [ ] Add error handling in cases of login failure, already wished all friends etc.



Feel free to contribute. Pull Requests are welcome. :)
