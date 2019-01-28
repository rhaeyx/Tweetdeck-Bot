"""
    This file works with TweetBot.py

    TweetDeck-Bot project by rhaeyx.
    https://github.com/rhaeyx/Tweetdeck-Bot
"""
import TweetBot

bot = TweetBot.TweetBot()

# Set the name to your .txt file
file_name = 'tweets.txt'

"""
    bot.start(
                file_name, # File name
                [(12,30,'pm'),  # (hour, min, am/pm)
                (3,30,'pm'),    # Add more or take away some
                (4,30,'pm'),    # totally up to you
                (5,30,'pm'),
                (6,30,'pm'),
                (7,30,'pm'),
                (8,30,'pm')],
                (1,31)          # Starting date (month, day)
            )
"""

bot.start(
            file_name,  
            [(12, 30, 'pm'),  
            (3, 30, 'pm'),    
            (4, 30, 'pm')],
            (11, 8)          
        )
