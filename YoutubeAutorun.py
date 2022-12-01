"""
@Author: Yen Peishan
@Update: May 29th, 2020

@How to use?
    SETTING:
        |--Part1: Set your url.
        |--Part2: Set your LOOP,VEDIOTIME.
            LOOP for run the vedio(eg.TWICE "Talk that Talk" M/V) how many times;
            VEDIOTIME for how many seconds you want to run the vedio.
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
#from selenium.webdriver.common.keys import Keys
import time
import random

#Setting:
#Part1: Set your url here!
url='https://www.youtube.com/watch?v=k6jqx9kZgPM&ab_channel=JYPEntertainment'
#Part2: Set your LOOP,VEDIOTIME here!
#LOOP for run your vedio(eg.Twice mv) how many times;
#VEDIOTIME for how many seconds you want to run the vedio.
LOOP,VEDIOTIME=3,20

#driver = webdriver.Chrome(ChromeDriverManager().install())
for i in range(LOOP):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdrive.Chrome("./chromedriver")
    driver.get(url)
    driver.refresh()
    element=driver.find_element_by_xpath("//*[@class='ytp-large-play-button ytp-button']")
    element.click()
    time.sleep(VEDIOTIME+random.randint(0,10))
    
    driver.close()