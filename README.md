# OKCUPIDBOT

Okcupid bot is a python3 - Selenium bot created for automating the monotonous process of liking a person's profile and sending an introduction message to that person on [Okcupid](http://www.okcupid.com)

## RUNNING THE SCRIPT

Following is the proccess of running this python script using the following commands:

1. Install python3 in your system.
```bash
sudo apt-get install python3.6
```
2. Install pip for python3
```bash
sudo apt-get install python3-pip
```
3. Install selenium in your folder 
```bash
sudo pip install selenium
```
4. Download chromium web driver from [Chromedriver for Selenium](http://chromedriver.chromium.org/) and install it using the following commands:
```bash
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```
5. Run the script with -i (interative flag) of python
```bash
python3 -i okcupidbot.py
```

## AUTHORS
[Narottam Singh Bisht](http://www.narottambisht.github.io)

Full Stack Developer (Javascript)