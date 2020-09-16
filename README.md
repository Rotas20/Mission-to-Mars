# Web Scraping Information About Mars

![mission_to_mars](Images/mission_to_mars.png)

This repo features a web application that scrapes various websites for data related to the Mission to Mars, displayed on a a single HTML page. 
Scraped data is stored in MongoDB and rendered through Flask templating to display the information on the front end. 


Initial scraping code is written in Jupyter Notebook using BeautifulSoup, Pandas, and Requests/Splinter.

### Sources scraped:

NASA Mars News scraped with Python

*https://mars.nasa.gov/news/


JPL Mars Space Images - Featured Image scraped with Splinter

*  https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

Mars Weather scraped from Twitter with Regular Expression Patterns

* https://twitter.com/marswxreport?lang=en

Mars Facts scraped with Pandas

* https://space-facts.com/mars/

Mars Hemispheres scraped with Python

* https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars




