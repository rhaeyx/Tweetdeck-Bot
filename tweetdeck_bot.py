from selenium import webdriver
from time import sleep
from random import randint

class tweetdeck:

    def __init__(self, username='username', password='password'):
        self.username = username
        self.password = password

    def open_tweetdeck(self):
        self.chrome = webdriver.Chrome('chromedriver.exe')
        self.chrome.get('https://tweetdeck.twitter.com')
    
    def login(self):
        self.chrome.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/div[1]/a').click()
        sleep(5)
        username = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        username.send_keys(self.username)
        password = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
        password.send_keys(self.password)
        sign_in = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
        sign_in.click()

    def set_month(self, current_month, target_month, current_year, target_year):
        months_dict = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 
                       'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 
                       'September': 9, 'October': 10, 'November': 11, 'December': 12}

        current_month = months_dict[current_month]
        current_year = int(current_year)

        clicks = target_month - current_month
        month_btn = ''

        if clicks == 0:
            return
        elif clicks > 0:
            month_btn = self.chrome.find_element_by_xpath('//*[@id="next-month"]')
        else:
            month_btn = self.chrome.find_element_by_xpath('//*[@id="prev-month"]')
            if target_year != current_year:
                diff = target_year - current_year
                clicks += (12 * diff)

            clicks = abs(clicks)

        for click in range(clicks):
            month_btn.click()
             
    def fill_up(self, text, hour, minute, period, month, day, year):
        """
            fill_up(text, hour, minute, period, month, day, year)
            
            input types: 
            hour - int        day - int
            minute - int      year - int
            period - str      month - int
        """
        textbox = self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[7]/textarea')
        textbox.send_keys(text)

        sched_tweet = self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[13]/button')
        sched_tweet.click()

        hour_box = self.chrome.find_element_by_xpath('//*[@id="scheduled-hour"]')
        hour_box.send_keys('\b\b'+str(hour))
        
        minute_box = self.chrome.find_element_by_xpath('//*[@id="scheduled-minute"]')
        minute_box.send_keys('\b\b'+str(minute))

        period_btn = self.chrome.find_element_by_xpath('//*[@id="amPm"]')
        if period_btn.text != period.upper():
            period_btn.click()
            sleep(0.5)

        month_text = self.chrome.find_element_by_xpath('//*[@id="caltitle"]').text
        current_month, current_year = month_text.split(' ')
        self.set_month(current_month, month, current_year, year)

        date = self.chrome.find_element_by_link_text(str(day))
        date.click()

        submit_btn = self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div[12]/div/div/button')
        submit_btn.click()
   
    def start(self, 
              source='tweets.txt',
              starting_date='12-09-2019',
              time_slots=[(7, 00, 'AM'), (12, 30, 'PM'), (4, 30, 'PM'), (5, 00, 'PM'),
                          (5, 30, 'PM'), (6, 30, 'PM'), (7, 30, 'PM'), (8, 30, 'PM')]):
    
        maximum_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        print("""
            Welcome to TweetDeck-Bot.py by rhaeyx
            Please consider giving this repo a star. 
            https://github.com/rhaeyx/Tweetdeck-Bot\n\n
        """)

        print('[TweetDeck_Bot] Starting bot...')

        self.open_tweetdeck()
        sleep(5) 

        print('[TweetDeck_Bot] Logging in...')
        self.login()
        sleep(5)
        print('[TweetDeck_Bot] Logged in.')

        starting_date = starting_date.split('-')
        month = int(starting_date[0])
        day = int(starting_date[1])
        year = int(starting_date[2])

        counter = 0

        print('[TweetDeck_Bot]Reading tweets to be scheduled...')
        lines = ''
        with open(source, 'r') as f:
            f = f.read()
            lines = f.split('\n')

        print('[TweetDeck_Bot]', len(lines), 'tweets found.')
        print('[TweetDeck_Bot] Removing text, that exceed the twitter character limit...')
        char_limit = 280
        for line in lines:
            if len(line) > char_limit:
                lines.remove(line)
        print('[TweetDeck_Bot]', len(lines), 'total number of tweets after purge.')

        print('[TweetDeck_Bot] Scheduling...\n')

        while len(lines) != 0:
            print('[TweetDeck_Bot] Tweets for:', '-'.join([str(month), str(day), str(year)]))
            for time_slot in time_slots:

                if len(lines) == 0:
                    break

                hour = time_slot[0]
                minute = time_slot[1]
                period = time_slot[2]

                random_index = randint(0, len(lines)-1)
                line = lines.pop(random_index)
                print('[TweetDeck_Bot] Tweet #'+str(counter), 'will be tweeted on ',':'.join([str(hour), str(minute)]), period)
                self.fill_up(line, hour, minute, period, month, day, year)
                counter += 1
                sleep(2)

            if day == maximum_days[month]: 
               
                if month == 12: 
                    month = 1
                    day = 1
                    year += 1
                else: 
                    month += 1
                    day = 1
            else: 
                day += 1 
            
        print('[TweetDeck_Bot] Total number of tweets:', counter)
        print('[TweetDeck_Bot] Thanks for using TweetDeck_Bot.py')
        print('[TweetDeck_Bot] Consider following me on twitter\n https://twitter.com/rhaeyx')

    def delete_tweets(self):
        
        self.open_tweetdeck()
        sleep(5) 
        self.login()
        sleep(5)
       
        while True:
            try:
                del_icon = self.chrome.find_element_by_xpath('//*[@id="container"]/div/section[2]/div/div[1]/div[1]/div[5]/div/article[1]/div/div[1]/a[2]')
                del_icon.click()
            except:
                pass
    
