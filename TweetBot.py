"""
    tweetdeck-bot.py v 1.0 - rhaey
    TweetDeck form fill-up bot. To fill up and schedule your tweets.

    0. Check the page if it has loaded.
    1. Click text field.
    2. Type in text field.
    3. Click schedule tweet.
    4. Scroll down.
    5. Click on hour.
    6. Delete the text, and type the hour wanted.
    7. Move to minute option, with tab.
    8. Move to the AM/PM option, and change accordingly.
    9. Click the day.
    10. Click the tweet button.
"""

import pyautogui
import time
from datetime import datetime
from math import floor

class TweetBot:
    tweetButton = (408,465)
    tweetButtonColor = (149,189,220)
    textField = (325,350)
    schedTweetButton = (325,580)
    hourBox = (255,450)
    originDay = (310,530) # Top of the calendar
    originDate = 1
    sendTweetButton = (385,280)

    def __init__(self, starting_date):
        self.originDate = starting_date - 1

    def loaded(self):
        # Check if the page have been loaded.
        if pyautogui.pixelMatchesColor(self.tweetButton[0], self.tweetButton[1], self.tweetButtonColor):
            return True
        return False

    def type_in_textfield(self, text):
        # I use move and click, cause directly clicking has a high chance it will cause some issues.
        pyautogui.moveTo(self.textField[0], self.textField[1], duration=1)
        pyautogui.click()
        pyautogui.typewrite(text, interval=0.10)

    def sched_tweet(self, hour, min, m): # m is am or pm
        pyautogui.moveTo(self.schedTweetButton[0], self.schedTweetButton[1], duration=1)
        pyautogui.click() # Click sched tweet button.
        time.sleep(1) # Add some delay to let the calendar open up.
        pyautogui.scroll(-300)
        pyautogui.moveTo(self.hourBox[0], self.hourBox[1]) # Focus on the hour input box.
        pyautogui.click()
        pyautogui.typewrite('\b\b'+str(hour)+'\t', interval=0.5) # Input hour then hit tab
        pyautogui.typewrite('\b'+str(min), interval=0.5) # Input min
        if m.upper() == 'PM' and self.am_pm() == 'PM': #
            return True # return something to stop the code from running.
        else:
            pyautogui.click(340,450)

    def click_day(self, day):
        pyautogui.moveTo(self.originDay[0], self.originDay[1], duration=2)
        pyautogui.click()
        time.sleep(2)
        numOfTabs = day - self.originDate + 8
        pyautogui.typewrite('\t' * numOfTabs , interval=0.20 )
        time.sleep(2)
        pyautogui.typewrite('\n' * 2)

    def am_pm(self):
        # Check a specific pixel on the screen, that pixel is the top-left tip of the P in PM
        # If that color is not white, that means its PM, if its white that means its AM
        pixelCoord = (331,446)
        pixelColor = (29,161,242)
        if pyautogui.pixelMatchesColor(pixelCoord[0],pixelCoord[1],pixelColor):
            return 'PM'
        return 'AM'

    def send_tweet(self):
        pyautogui.moveTo(self.sendTweetButton[0], self.sendTweetButton[1], duration=1)
        pyautogui.click()

    def tweetbot(self, text, hour, min, m, day):
        while not self.loaded() :
            time.sleep(1)
        self.type_in_textfield(text)
        self.sched_tweet(hour, min, m)
        time.sleep(2)
        self.click_day(day)
        self.send_tweet()

        # Needs a text file, two 'times' for when to post
    def TwitterBotStart(self, txt, time_a, time_b):
        part_of_the_day = { '12': {'hour': 12, 'min': 30},
                            '3' : {'hour':  3, 'min': 00},
                            '4' : {'hour':  4, 'min': 50},
                            '6' : {'hour':  6, 'min': 45}
                           }

        file = open(txt, 'r')
        file = file.read()
        lines = file.split('\n')
        print(lines)

        counter = 1
        time_to_post = (part_of_the_day[time_a]['hour'], part_of_the_day[time_a]['min'])
        post_day = self.originDate + 1 # First day to post

        for line in lines:
            if counter % 2 == 0: # If counter is even post on the other time
                time_to_post = (part_of_the_day[time_b]['hour'], part_of_the_day[time_b]['min'])

            self.tweetbot(line, time_to_post[0], time_to_post[1], 'pm', floor(post_day))

            counter += 1
            post_day += 0.5

        print('Done. Scheduled ', counter, ' tweets.')
        input('Press enter to close.')
