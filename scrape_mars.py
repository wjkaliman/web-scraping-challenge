# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Mission to Mars 


from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd
import time

# %% [markdown]
# Mars news scraping

# %%
def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # %%
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url) 

    # %% [markdown]
    # Time to scrape

    # %%
    html = browser.html
    soup = bs(html, 'html.parser') 


    # %%
    time.sleep(1)
    news_title = soup.find("div",class_="content_title").text
    try:
        news_p = soup.find("div", class_="article_teaser_body").text
    except:
        news_p = ""
    print(f"Title: {news_title}")
    print(f"Para: {news_p}")

    # %% [markdown]
    #  JPL image scraping

    # %%
    jpl_url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url_image)


    # %%
    full_image = browser.find_by_id("full_image")
    full_image.click()


    # %%
    more_info = browser.find_link_by_partial_text("more info")
    more_info.click()


    # %%
    html = browser.html
    soup = bs(html, 'html.parser')


    # %%
    #look for the tag(img), find the class. will output a list
    # and look for the source
    images = soup.find_all("img", class_= "main_image")
    images[0]["src"]


    #use base url from above and add {} with list and source
    featured_image_url = f"https://www.jpl.nasa.gov{images[0]['src']}"
    featured_image_url

    # %% [markdown]
    # Mars Weather
    # %% [markdown]
    # * Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.
    # * **Note: Be sure you are not signed in to twitter, or scraping may become more difficult.**
    # * **Note: Twitter frequently changes how information is presented on their website. If you are having difficulty getting the correct html tag data, consider researching Regular Expression Patterns and how they can be used in combination with the .find() method.**

    # %%
   
    twitter = "https://twitter.com/marswxreport?lang=en"

    browser.visit(twitter)
    # time.sleep help the length of loading the web page
    time.sleep(5)
    twit_html = browser.html
    twit_soup = bs(twit_html, 'html.parser')
    #twitt = twit_soup.find('div') 

    # find the div based on the attribute
    mars_weather = twit_soup.find_all("div",attrs={"data-testid":"tweet"})
   

    # %%
    # read a specific child to get the tweet
    weather = mars_weather[1].text

    # %% [markdown]
    # use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.

    # %%
    facts_url = 'https://space-facts.com/mars'
    t_df = pd.read_html(facts_url)[0]
    t_df = t_df.rename(columns={0:'Mars Planet Profile',1:''})
    t_df = t_df.set_index('Mars Planet Profile')
    t_df

    # %% [markdown]
    # Use Pandas to convert the data to a HTML table string.
    # mars_facts ouput

    # %%
    html_table = t_df.to_html()
    html_table

    

    # %%
    # grabbing 4 images
    USGS_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(USGS_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    
    mars_hemi = []

    photo = browser.find_by_css('a.product-item h3')
    for i in range(len(photo)):
        # code below grabs the link
        time.sleep(1)
        browser.find_by_css('a.product-item h3')[i].click()
        Mars_dict = {}
        sample = browser.find_link_by_text("Sample").first
        print(sample["href"])
        link = sample["href"]
        # code below grabs the title
        title = browser.find_by_css("h2.title").text
        print(title)
        # putting back the titles and links in a dictionary below
        Mars_dict["title"]=title
        Mars_dict["img_url"]=link
        # were taking the 2 dictionaries and sending them back to the empty mars_hemi 
        mars_hemi.append(Mars_dict)
        # below tells the browser to go back and get the second image and 3rd and so on
        browser.back()
    browser.quit()

    data = {
        "news_title":news_title,
        "news_para":news_p,
        "featured_image_url":featured_image_url,
        "mars_weather":weather,
        "mars_facts":facts_url[0],
        "mars_hemi":mars_hemi
    }
    print(data)
    return data
    #mars_hemi



    
