# AutoWish
AutoWish is an automation script which wishes 'Happy birthday' to all your facebook friends who have their birthday today by posting on their facebook timelines.

It uses Selenium WebDriver to create a browser object and login to your facebook ID after you enter your login credentials as input when prompted for.

The script runs on python3

### Install requirements
Selenium:
```
pip install selenium
```
Chrome WebDriver: [Install](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### How to use
Clone the repository and run in terminal:
```
cd
git clone https://github.com/akshatjain02/AutoWish.git
cd AutoWish
sudo pip install -U -r requirements.txt
python3 FB_Wisher.py
```
You can also download the ZIP file, extract it, and run FB_Wisher.py script in a text editor like Sublime Text. For enabling console inputs in Sublime Text, see point 3 under Notes.

### Notes
1. When creating a browser instance for the Chrome WebDriver in the code, set the path argument as the location of the chromedriver executable file.
2. The password input may be echoed. Be careful while testing the script in presence of other people.
3. If you want to test the script on Sublime Text Editor, which does not support console inputs in a build, then you can use [SublimeREPL](https://github.com/wuub/SublimeREPL) by following this [link](https://stackoverflow.com/questions/10604409/sublime-text-2-console-input).
4. Enter your FB username and password (echoed) as console input when asked.

### Bugs/TODOs
- [ ] Make the password input unechoed.
- [ ] Add error handling in cases of login failure, already wished all friends etc.



Feel free to contribute. Pull Requests are welcome. :)
