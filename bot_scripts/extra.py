from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class extra:
    """
        Features:
        > Follow ()
        > Like ()
        > Copy Tweets ()

        Params:
            username = 'rhaeyx', type(username) == string
            password = 'password', type(password) == string
            headless = True, type(headless) == boolean
    """

    def __init__(self,
                 username='rhaeyx',
                 password='password',
                 headless=True):
        self.headless = headless
        self.username = username
        self.password = password

    # Set up
    def open_twitter(self):
        options = Options()
        options.headless = self.headless
        options.add_argument('--log-level=3')
        options.add_argument('--silent')
        self.chrome = webdriver.Chrome('chromedriver.exe', options=options)
        self.chrome.get('https://twitter.com/login')

    def login(self):

        print('[TweetDeck_Extra] Logging in to', self.username)
        # Type in username
        username = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        username.send_keys(self.username)

        # Type in password
        password = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
        password.send_keys(self.password)

        sign_in = self.chrome.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
        sign_in.click()
        print('[TweetDeck_Extra] Logged in to', self.username)

    def like(self, to_like=100):
        """
            When ran, will open a new instance of chrome and log-in to the twitter account set, with the
            initialization of the class. Then like a number of n tweets based on the to_like parameter
            by default, it would like 100 tweets. After doing that, it will close the chrome instance.

            to_like is the number of tweets to like, by default it is set to 100.
            type(to_like) == integer

        """

        self.open_twitter()
        sleep(10)

        self.login()
        sleep(10)

        counter = 1
        while True:

            like_btns = self.chrome.find_elements_by_css_selector('button.ProfileTweet-actionButton.js-actionButton.js-actionFavorite')

            if counter > to_like:
                break

            for like_btn in like_btns:
                try:
                    if counter > to_like:
                        break
                    like_btn.click()
                    print('[TweetDeck_Extra] Like #' + str(counter))
                    counter += 1
                    sleep(0.5)
                except:
                    continue

        print('[TweetDeck_Extra] Liked a total of ' + str(counter) + ' tweets.')
        print('[TweetDeck_Extra] Thank you for using TweetDeck_Bot.')
        print('[TweetDeck_Extra] Closing chrome instance...')
        self.chrome.close()

    def follow(self, to_follow=50):
        """
            Docstringggg.

        """

        self.open_twitter()
        sleep(10)

        self.login()
        sleep(10)

        # The first account in the homepage, the owner of the first tweet.
        source_account = self.chrome.find_element_by_css_selector('div.stream-item-header > a')
        source_account.click()

        sleep(5)
        followers_btn = self.chrome.find_element_by_partial_link_text('Followers')
        followers_btn.click()
        sleep(5)

        counter = 0

        while True:

            while counter < to_follow:

                follow_btns = self.chrome.find_elements_by_css_selector('button.EdgeButton.EdgeButton--secondary.EdgeButton--small.button-text.follow-text')

                for follow_btn in follow_btns:
                    try:
                        if counter >= to_follow:
                            break
                        follow_btn.click()
                        counter += 1
                        print('[TweetDeck_Extra] Follow #' + str(counter))
                        sleep(0.5)
                    except:
                        continue

            if counter > to_follow:
                break

        print('[TweetDeck_Extra] Followed a total of ' + str(counter) + ' accounts.')
        print('[TweetDeck_Extra] Thank you for using TweetDeck_Bot.')
        print('[TweetDeck_Extra] Closing chrome instance...')
        print('Follow me on twitter: twitter.com/rhaeyx')
        self.chrome.close()
