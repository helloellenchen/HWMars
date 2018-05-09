#Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
#import dependencies
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from selenium import webdriver
import requests as req
import re

from splinter import browser
from selenium import webdriver
# Scrape function
def Scrape():

	print("COMMENCING SCRAPE")
    print("----------------------------------")

    # Empty dictionary
    mars_dict = {}

    # ## NASA Mars News

    # Mars News URL
    url = "https://mars.nasa.gov/news/"

    # Retrieve page with the requests module
    html = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # Get title & description
    news_title = soup.find('div', 'content_title').text	
    news_p = soup.find('div', 'rollover_description_inner').text

    # Adding to dict
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p

    print("NEWS TITLE & DESCRIPTION")


     # ## JPL Mars Space Images

    # JPL Mars URL
    !which chromedriver
    # Setting up splinter
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path, headless=False)
	url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url_image)
	#Getting the base url
	from urllib.parse import urlsplit
	base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
	print(base_url)
	#Design an xpath selector to grab the image
	xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"
	#Use splinter to click on the mars featured image
	#to bring the full resolution image
	results = browser.find_by_xpath(xpath)
	img = results[0]
	img.click()
	#get image url using BeautifulSoup
	html_image = browser.html
	soup = bs(html_image, "html.parser")
	img_url = soup.find("img", class_="fancybox-image")["src"]
	featured_image_url = base_url + img_url
	print(featured_image_url)
	mars_dict["featured_image_url"] = featured_image_url
	print("FEATURED IMAGE")

	#3. Mars weather 
	#get mars weather's latest tweet from the website
	url_weather = "https://twitter.com/marswxreport?lang=en"
	browser.visit(url_weather)
	html_weather = browser.html
	soup = bs(html_weather, "html.parser")
	#temp = soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
	mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
	print(mars_weather)
	mars_dict["mars_weather"] = mars_weather
    print("WEATHER ACQUIRED")

    #4. Mars facts
	url_facts = "https://space-facts.com/mars/"

	# Retrieve page with the requests module
    html = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # Empty dictionary for info
    mars_profile = {}

    df_mars_facts = table[0]
	df_mars_facts.columns = ["Parameter", "Values"]
	df_mars_facts.set_index(["Parameter"])
	mars_html_table = df_mars_facts.to_html()
	mars_html_table = mars_html_table.replace("\n", "")
	mars_html_table
































	