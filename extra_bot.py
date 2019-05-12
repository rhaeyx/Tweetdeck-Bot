"""
    extra_bot.py, a project by rhaeyx
    Please consider giving this repo a star. 
    https://github.com/rhaeyx/Tweetdeck-Bot

    Contents:
        tweetdeck.py - source code
        bot.py(this) - file to execute
        tweets.txt - Example text file
"""
from bot_scripts.extra import extra

# Account
bot = extra(username='rhaeyx', password='rhaeyx')

"""
    LIKE TWEETS:
        to_like - amount of tweets to like
"""
bot.like(to_like=200)

"""
    FOLLOW ACCOUNTS:
        to_follow - amount of accounts to follow
"""
bot.follow(to_follow=50)

