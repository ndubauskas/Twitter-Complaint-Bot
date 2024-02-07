from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

PROMISED_UP = 100
PROMISED_DOWN = 10
USERNAME = os.environ.get("email")
PASSWORD = os.environ.get("password")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(options=chrome_options)
    def get_internet_speed(self):

        self.driver.get("https://fast.com/")
        time.sleep(60)

        self.down = float(self.driver.find_element(By.XPATH,value='//*[@id="speed-value"]').text)
        show_more_info_button = self.driver.find_element(By.XPATH,value='//*[@id="show-more-details-link"]')
        show_more_info_button.click()
        self.up = float(self.driver.find_element(By.XPATH,value='//*[@id="upload-value"]').text)
        print(f"Upload: {self.up}\n Download: {self.down}")

    def tweet_at_provider(self):
        # self.down = 10
        # self.up = 2
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get("https://twitter.com/home")
            time.sleep(5)
            username = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            username.click()
            username.send_keys(USERNAME,Keys.ENTER)
            time.sleep(10)
            password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.click()
            password.send_keys(PASSWORD,Keys.ENTER)
            time.sleep(30)

            draft = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            draft.click()
            draft.send_keys(f"WhY InterNEt sloWW i Pay for {PROMISED_UP} up AND  {PROMISED_DOWN} dOWn but right NOw Ima getINnGG {self.up} Up {self.down}DoWN",Keys.ENTER)
            post_button = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
            post_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()