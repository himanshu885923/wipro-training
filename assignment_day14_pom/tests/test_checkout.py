from pages.cart_page import CartPage


def test_checkout(driver):

    cart = CartPage(driver)

    cart.open_cart()

    modal = cart.click_place_order()

    data = {
        "name": "Rahul",
        "country": "India",
        "city": "Delhi",
        "card": "123456789",
        "month": "05",
        "year": "2026"
    }

    modal.fill_purchase_form(data)

    modal.click_purchase()

    assert (
        modal.get_success_message()
        == "Thank you for your purchase!"
    )