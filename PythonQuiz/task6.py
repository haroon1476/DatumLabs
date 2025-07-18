
orders = [
    { "product":"apple" , "quantity":5},
    {"product":"banana" , "quantity":2},
    { "product":"apple" , "quantity":3},
]


totalOrder = {} # to store unique orders and their sum

for order in orders:

    product = order["product"]
    quantity = order["quantity"]

    # print(f"Product = {product}")
    # print(f"Quantity = {quantity}")

    if product in totalOrder:
        # if already in the dict, adding the value
        totalOrder[product] += quantity
    else:
        # if not, then simply inserting in the dict
        totalOrder[product] = quantity

print(totalOrder)
