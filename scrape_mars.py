import pandas as pd
from bs4 import BeautifulSoup as bs
from flask import Flask, render_template, redirect
from splinter import Browser
import requests
import pymongo
from pprint import pprint
import re
import time


def scrapeNews():

    executable_path = {'executable_path': '/Users/star/Downloads/chromedriver-2'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/?page=0&per_page=1&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    news_soup = bs(html, 'html.parser')
    results_title = news_soup.find_all('div', class_="content_title")[1].text
    results_body = news_soup.find_all('div', class_="article_teaser_body")[0].text

    return [results_title, results_body]
    

            

def scrapeFeaturedimg():
    executable_path = {'executable_path': '/Users/star/Downloads/chromedriver-2'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    full_img = browser.find_by_id("full_image").click()
    time.sleep(2)
    more_info = browser.links.find_by_partial_text("more info").click()
    time.sleep(2)   
    html = browser.html
    image_soup = bs(html, 'html.parser')
    ft_img = image_soup.select_one(".lede a").get("href")
    featured_image_url = ("https://www.jpl.nasa.gov/" + ft_img)
    return featured_image_url


def scrapeWeather():
    executable_path = {'executable_path': '/Users/star/Downloads/chromedriver-2'}
    browser = Browser('chrome', **executable_path, headless=False)
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)
    time.sleep(5)
    html = browser.html
    twitter_soup = bs(html, 'html.parser')
    mars_weather = twitter_soup.find('span',text=re.compile(r'InSight')).text
    return mars_weather
    
def scrapeFacts():
    df = pd.read_html('https://space-facts.com/mars/')
    one_df = df[1]
    html_table = one_df.to_html(classes="table table-striped", index=False)
    return html_table
   
 
def scrapeHemispheres():

#cerb 
   
    executable_path = {'executable_path': '/Users/star/Downloads/chromedriver-2'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)
    cerb = browser.find_by_css("a.product-item h3").click()
    html = browser.html
    image_soup = bs(html, 'html.parser')
    cerb_url = image_soup.select_one("div #wide-image img.wide-image").get("src")
    base = 'https://astrogeology.usgs.gov/'
    cerb_img = (base + cerb_url)
    cerb_name = image_soup.h2.text
    cerb_dict = {
    "title": cerb_name,
    "img_url": cerb_img
    }
 



    # ### Valles
    executable_path = {'executable_path': '/Users/star/Downloads/chromedriver-2'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)
    valles = browser.find_by_css("a.product-item h3")[3].click()
    html = browser.html
    image_soup = bs(html, 'html.parser')
    valles_url = image_soup.select_one("div #wide-image img.wide-image").get("src")
    base = 'https://astrogeology.usgs.gov/'
    valles_img = (base + valles_url)
    valles_title = image_soup.h2.text
    valles_dict = {
        "title": valles_title,
        "img_url": valles_img
    }





    # ### Schiaparelli Hemisphere Scraping
    executable_path = {'executable_path': '/Users/star/Downloads/chromedriver-2'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)
    sch = browser.find_by_css("a.product-item h3")[1].click()
    html = browser.html
    image_soup = bs(html, 'html.parser')
    sch_url = image_soup.select_one("div #wide-image img.wide-image").get("src")
    base = 'https://astrogeology.usgs.gov/'
    sch_img = (base + sch_url)
    schi_title = image_soup.h2.text
    schi_dict = {
        "title": schi_title,
        "img_url": sch_img
    }




    # ### Syrtis Major Hemisphere Scraping
    executable_path = {'executable_path': '/Users/star/Downloads/chromedriver-2'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)
    syr = browser.find_by_css("a.product-item h3")[2].click()
    html = browser.html
    image_soup = bs(html, 'html.parser')
    syr_url = image_soup.select_one("div #wide-image img.wide-image").get("src")
    base = 'https://astrogeology.usgs.gov/'
    syr_img = (base + syr_url)
    syr_title = image_soup.h2.text
    syr_title

    syr_dict = {
        "title": syr_title,
        "img_url": syr_img
    }
    


    hemisphere_image_urls = []

    hemisphere_image_urls.append(valles_dict)
    hemisphere_image_urls.append(cerb_dict)
    hemisphere_image_urls.append(schi_dict)
    hemisphere_image_urls.append(syr_dict)

    return hemisphere_image_urls

def scrapeAll():

    
    results_title, results_body = scrapeNews()

    all_dict = {

        "MarsNewsTitle" : results_title,
        "MarsNewsParagraph" : results_body,
        "MarsImage" : scrapeFeaturedimg(),
        "MarsWeather" : scrapeWeather(),
        "MarsFacts" : scrapeFacts(),
        "MarsHemispheres" : scrapeHemispheres()
     }
    return all_dict



if __name__ == "__main__":
    print("I was called directly; success!")
    