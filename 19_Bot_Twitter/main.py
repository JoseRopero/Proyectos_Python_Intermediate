import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


class InternetSpeedTwitterBot:
    def __init__(self, options):
        self.driver = webdriver.Chrome(options)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()
        time.sleep(60)

        self.up = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                 '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        self.down = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                   '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(5)

        email = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        email.send_keys(os.environ['TWITTER_EMAIL'], Keys.RETURN)
        time.sleep(5)

        usuario = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        usuario.send_keys('Jose_8382_09', Keys.RETURN)
        time.sleep(5)

        password = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        password.send_keys(os.environ['TWITTER_PASSWORD'], Keys.RETURN)
        time.sleep(10)

        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div['
                                                       '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                       '1]/div/div/div/div[2]/div['
                                                       '1]/div/div/div/div/div/div/div/div/div/div['
                                                       '1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div['
                                                      '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                      '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(chrome_options)
bot.get_internet_speed()
bot.tweet_at_provider()
