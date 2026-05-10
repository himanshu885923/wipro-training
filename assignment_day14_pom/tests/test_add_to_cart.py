from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage

def test_add_product(driver):

    home = HomePage(driver)

    home.open()

    category = home.click_laptops()

    category.select_product("Sony vaio i5")

    product_page = ProductDetailsPage(driver)

    product_page.add_product_to_cart()