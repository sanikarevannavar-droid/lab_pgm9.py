def product_details(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price:.2f}"
    )


# Main program
if __name__ == "__main__":
    result = product_details(101, "Washing Machine", 5, 55000)
    print(result)
