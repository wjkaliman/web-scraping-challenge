# web-scraping-challenge
build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.
Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.
Scrape https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars using splinter for the full siaze JPG image
Save url string for image.
Visit the Mars Weather twitter account (https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text 
Visit the Mars Facts webpage (https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Visit the USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. 
