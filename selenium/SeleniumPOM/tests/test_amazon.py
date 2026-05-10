import time

import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    print("\nOpened Amazon Homepage. Title & URL verified.")

@pytest.mark.parametrize("searchproduct", [
    ("wireless mouse"), ("shoes")
])
def test_search_product(driver, searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print("\nSearch result page loaded successfully")
    time.sleep(10)

def test_find_elements_amazon(driver):
    productlistingpage = ProductListingPage(driver)

    productlistingpage.find_product_title()
    val = productlistingpage.all_product()

    assert val, "No products found on Amazon search results!"

def test_brand_filter(driver):
    productlistingpage = ProductListingPage(driver)
    productlistingpage.select_brand_filter()
    val = productlistingpage.all_product()

    assert val, "No products found on Amazon search results!"

def test_brand_filter(driver):
    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter()

    assert  productlistingpage.check_product_titles_for_brand_filter('Logitech'), 'Brand filter did not apply'
