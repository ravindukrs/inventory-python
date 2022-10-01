#
# def inventory_app(inventory):
#     print("hi")
#
# def add_item(inventory, item):
#     print("Adding item")
#     inventory.push(item)
#

if __name__ == '__main__':
    inventory = []

    operation = input("Select Operation: Add_Vehicle, Check_Price, Create_Invoice, List_Inventory ")

    if operation == "Add_Vehicle":
        print("Add Vehicle Menu: ")
        make = input("Enter Make")
        model = input("Enter Model")
        qty = input("Enter Quantity")
        price = input("Enter Price")
        common = make+model

        item_object = {
            "Make": make,
            "Model": model,
            "Quantity": qty,
            "Price": price,
            "Common": common
        }

        if not any(d['Common'] == common for d in inventory):
            inventory.push(item_object)
        else:
            print("Sorry you already have this item in invetory. Incrementing stock is not currently supported")

    elif operation == "Check_Price":
        print("Check Price Menu: ")
        make = input("Enter Make")
        model = input("Enter Model")
        common = make + model
        if any(d['Common'] == common for d in inventory):
            result = next((item for item in inventory if item["Common"] == common), None)
            print(result["Price"])
    # elif operation >= 18:
    #     print("You are allowed to party")
    else:
        "Invalid Operation"
