from selenium import webdriver

# create a new Firefox browser instance
driver = webdriver.Firefox()

# navigate to the website
driver.get("https://www.example.com")

# find the search bar element by its ID and type in a search term
search_bar = driver.find_element_by_id("search-bar")
search_bar.send_keys("Selenium automation")

# find the search button element by its CSS class and click it
search_button = driver.find_element_by_class_name("search-button")
search_button.click()

# assert that the search results page contains the expected text
assert "Search results for 'Selenium automation'" in driver.page_source

# close the browser
driver.quit()
