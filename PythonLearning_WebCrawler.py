import logging
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#function to extract the text of an element based on the css name inside the dom element
def check_exists_by_css_selector(domelement, cssname):
    value = "Not Available"
    try:
        value = domelement.find_element_by_css_selector(cssname).text
    except NoSuchElementException:
        return "Not Available"
    return value

#open a browser session and navigate to the search results page using the url
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options)
browser.get("https://www.travelsite.com/searchresults.html?checkin_month=8&checkin_monthday=17&checkin_year=2018&checkout_month=8&checkout_monthday=18&checkout_year=2018&class_interval=1&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&no_rooms=1&offset=0&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&src=index&src_elem=sb&ss=SanFrancisco%2C%20California%2C%20USA&ss_all=0&ss_raw=SanFrancisco")


import pandas as pd
competitive_info = pd.DataFrame([(check_exists_by_css_selector(link, "span.sr-hotel__name"),
  check_exists_by_css_selector(link, "span.review-score-badge"),
  check_exists_by_css_selector(link, "td.roomPrice")
 ) for link in browser.find_elements_by_css_selector("div.sr_item")], columns = ['Name', 'Rating', 'Price'])

browser.quit()

#formatting the currency information with duckling wrapper
import duckling
duck = duckling.DucklingWrapper()
competitive_info['Curated'] = competitive_info['Price'].apply(lambda x: duck.parse_money(x))
competitive_info
