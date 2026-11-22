
from product import product_details

def test_product_details():
    expected = (
        "Product ID: 101\n"
        "Product Name: Washing Machine\n"
        "Quantity: 5\n"
        "Price: 55000.00"
    )

    assert product_details(101, "Washing Machine", 5, 55000) == expected


