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

from pyautogui import *
import time
from datetime import datetime
from math import floor
from random import randint

class TweetBot:
    """
        TweetBot(starting_day):
    """
    # Initialize variables for coords "(0,0)" and colors "(R, G, B)".
    tweet_btn = (0,0)
    tweet_btn_color = (0,0,0) 
    text_box = (0, 0) 
    sched_btn = (0, 0) 
    hour_box = (0, 0) 
    calendar = (0, 0) 
    period_btn = (0,0) # Period, am or pm.
    period_btn_color = (0,0,0) # R, G, B
    current_month = 1
    month_btn = (0,0)
    originDate = 0

    # Month: Days in a month. 1 for January and so on.
    maximum_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def setup(self):
        # Setup the coordinates for buttons, textbox and set the color.
        try:
            print('Setting up some variables and coordinates...')

            self.current_month = datetime.now().month
            print('1/7 - Current month is', self.current_month)

            self.tweet_btn = locateCenterOnScreen('tweet_btn.png')
            self.tweet_btn_color = screenshot().getpixel(self.tweet_btn)
            print('2/7 - Tweet button located.')

            self.text_box = locateCenterOnScreen('text_box.png')
            print('3/7 - Text box located.')

            self.sched_btn = locateCenterOnScreen('sched_btn.png')
            print('4/7 - Schedule button located.')
           
            click(self.sched_btn)
            scroll(-300)
            time.sleep(1)
            self.hour_box = locateCenterOnScreen('hour_box.png')
            print('5/7 - Time boxes located.')

            # If period_pm is not found, it will cause an error.
            try: 
                self.period_btn = locateOnScreen('period_pm.png')
            # Catch it, and then click the period box to set it to pm
            # then set the coordinates.
            except:
                click(locateCenterOnScreen('period_box.png'))
                moveRel(75,0, duration=0.2)
                click(clicks=2, interval=0.1)
                time.sleep(1)
                self.period_btn = locateOnScreen('period_pm.png')

            self.month_btn = locateCenterOnScreen('month_btn.png')

            # Get the bottom right pix, by adding top coord + height and left coord + width.
            self.period_btn = (self.period_btn[0] + self.period_btn[2], self.period_btn[1] + self.period_btn[3])
            self.period_btn_color = screenshot().getpixel((self.period_btn[0], self.period_btn[1]))
            print('6/7 - AM or PM box located.')

            self.calendar = locateCenterOnScreen('calendar.png') 
            print('7/7 - Calendar located.\nResetting.')
            click(locateCenterOnScreen('remove_btn.png'))
        except:
            print('ERROR: Make sure the tweetdeck dashboard for tweeting is open and visible\nand is showing the default dashboard.')

    def is_loaded(self):
        # Check if the page have been loaded.
        if pixelMatchesColor(self.tweet_btn[0], self.tweet_btn[1], self.tweet_btn_color):
            return True
        return False

    def type_in_textfield(self, text):
        # Click the text box and type in the text.
        click(self.text_box[0], self.text_box[1], duration=1)
        typewrite(text, interval=0.1)

    def sched_tweet(self, hour, min, period):
        click(self.sched_btn[0], self.sched_btn[1], duration=0.5) 
        # Add some delay to let the calendar open up and let the page scroll down.
        time.sleep(1) 
        scroll(-300) 
        time.sleep(1)
        # Click the hour input box and input hour and minute.
        click(self.hour_box[0], self.hour_box[1], clicks=2)
        typewrite('\b'+str(hour)+'\t', interval=0.1) 
        typewrite('\b'+str(min), interval=0.2) 
        if period.upper() == self.am_pm(): 
            return  
        else:
            click((self.period_btn[0], self.period_btn[1]))        

    def click_day(self, month, day):
        # Set month.
        self.set_month(self.current_month, month)

        # Click the day chosen. first_date is the coords for the day 1 of the month.
        first_date = (0,0)
        try:
            first_date = locateCenterOnScreen('1_active.png')
        except:
            first_date = locateCenterOnScreen('1_inactive.png')

        # Set day.
        click((first_date[0], first_date[1]), clicks=2)

        num_of_tabs = day - 1
        typewrite('\t' * num_of_tabs, interval=0.1)
        # Hit enter key two times to select that day.
        typewrite('\n\n')

    def am_pm(self):
        # Check a specific pixel on the screen, that pixel is the top-left tip of the P in PM
        # If that color is not white, that means its PM, if its white that means its AM
        if pixelMatchesColor(self.period_btn[0], self.period_btn[1], self.period_btn_color):
            return 'PM'
        return 'AM'

    def set_month(self, current_month, target_month):
        # Current month is provided by datetime function.
        difference = 0
        if current_month != target_month:
            difference = target_month - current_month
        moveTo(self.month_btn)
        click(clicks=difference, interval=0.5)



    def send_tweet(self):
        tweet_btn_coords = locateCenterOnScreen('active_tweet_btn.png')
        click(tweet_btn_coords)

    def input_bot(self, text, hour, min, period, month, day):
        # Text is the text to be tweeted.
        while not self.is_loaded() :
            time.sleep(1)
        self.type_in_textfield(text)
        self.sched_tweet(hour, min, period)
        # time.sleep(2)
        self.click_day(month, day)
        self.send_tweet()

       
    def TwitterBotStart(self, text_file, times, starting_date):
        """
            TwitterBotStart(textfile, [(hour, min, period),(hour, min, period),(hour, min, period)])        
            1. Text file with the tweets. 
            2. List of tuples, each tuple with an hour, min and period. (5,30,'am')
            3. starting_date = (MM, DD)
        """

        self.setup()

        lines = ''
        print('Opening', text_file, '...')
        with open(text_file, 'r') as f:
            f = f.read()
            lines = f.split('\n')

        month = starting_date[0]
        date = starting_date[1]
        counter = 0

        while len(lines) != 0:
            # time represents the time in the day.
            for time in times:
                # Select a random tweet.
                random_index = randint(0, len(lines)-1)
                line = lines.pop(random_index)
                self.input_bot(line, time[0], time[1], time[2], month, date)
                print('Scheduled for', str(time[0])+':'+str(time[1]), time[2],'=', line)
                counter += 1

            if date < self.maximum_days[month]:
                date += 1
            else: 
                month += 1
                date = 1
    
        print('Done. Scheduled ', counter, ' tweets.')
        input('Press enter to close.')

    if __name__ == '__main__':
        a = 1
