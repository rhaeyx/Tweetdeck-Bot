"""
    tweetdeck_bot.py, a project by rhaeyx
    Please consider giving this repo a star. 
    https://github.com/rhaeyx/Tweetdeck-Bot

    Contents:
        tweetdeck_bot.py - code for automating tweetdeck tweet.
        extra.py - code for automating likes and follows.
        bot.py(this) - file to execute
        extra_bot.py - file to execute for auto follow and like
        tweets.txt - Example text file
"""

from tweetdeck_bot import tweetdeck

# Set username and password
bot = tweetdeck(username='placeholder', password='placeholder')

# Start bot. Default values are just placeholders, change as you want.
"""
bot.start(starting_date='12-09-2019', FORMAT: MM-DD-YYYY
          time_slots = [(8, 30, 'PM'), FORMAT: (hour, min, period) period is 'AM' or 'PM'
                        (5, 30, 'PM'),
                        (6, 30, 'PM'), 
                        (7, 30, 'PM')],
          source='tweets.txt') 
          # Source file: file_name.txt, make sure to place the file in same folder, together with this
          # file and tweetdeck_bot.py
"""

# EXAMPLE:
bot.start(starting_date='12-09-2019',
          time_slots = [(8, 30, 'PM'),
                        (5, 30, 'PM'),
                        (6, 30, 'PM'), 
                        (7, 30, 'PM')],
          source='tweets.txt')

