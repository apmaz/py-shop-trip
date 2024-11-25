import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        file_config = json.load(file)

    for customer in file_config["customers"]:
        buyer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]["fuel_consumption"]
        )

        buyer.print_customer_name_and_money()
        price_in_shops = {}
        for shop in file_config["shops"]:
            shop = Shop(shop["name"], shop["location"], shop["products"])
            price = buyer.get_price_product_cart(shop, file_config)
            price_in_shops[shop] = price

        shop_with_min_price = min(price_in_shops, key=price_in_shops.get)
        min_price = price_in_shops[shop_with_min_price]

        if buyer.money < min_price:
            print(
                f"{buyer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            buyer.change_location_buyer(shop_with_min_price)
            buyer.print_check(shop_with_min_price)
            buyer.calculate_buyer_balance_of_money(min_price)
