"""
    tweetdeck_bot.py, a project by rhaeyx
    Please consider giving this repo a star. 
    https://github.com/rhaeyx/Tweetdeck-Bot

    Contents:
        tweetdeck_bot.py - code for automating tweetdeck tweet.
        extra.py - code for automating likes and follows.
        bot.py - file to execute for automating tweetdeck tweets.
        extra_bot.py(this) - file to execute for auto follow and like
        tweets.txt - Example text file
"""

from extra import extra

# Set username and password
bot = extra(username='placeholder', password='placeholder')

# Start bot. Default values are just placeholders, change as you want.

""" bot.start(to_like=100, to_follow=50) """

# EXAMPLE:
bot.start(to_like=100, 
          to_follow=50)


