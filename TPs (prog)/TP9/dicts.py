
def create_inventory(items):
    inventory = dict()
    for item in items:
        if item not in inventory:
            inventory[item] = items.count(item)
    return inventory


def add_items(inventory, items):
    inventory_2 = create_inventory(items)
    for mat in inventory_2:
        if mat in inventory:
            inventory[mat] = inventory[mat] + inventory_2[mat]
        else:
            inventory[mat] = inventory_2[mat]
    return inventory


def decrement_items(inventory, items):
    inventory_2 = create_inventory(items)
    for mat in inventory_2:
        if mat in inventory:
            inventory[mat] = inventory[mat] - inventory_2[mat]
    for mat in inventory:
        if inventory[mat] < 0:
            inventory[mat] = 0
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    listed_inventory = list()
    for mat in inventory:
        if inventory[mat] > 0:
            listed_inventory.append((mat, inventory[mat]))
    return listed_inventory
