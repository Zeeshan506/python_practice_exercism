"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart
     


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    current_cart = {}
    for item in notes:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    recipe_updates = dict(recipe_updates)
    for key,value in recipe_updates.items():
        ideas[key] = value
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    srted_cart = dict(sorted(cart.items()))
    return srted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment = {}

    for item in sorted(cart.keys(), reverse=True):
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            fulfillment[item] = [cart[item], aisle, refrigeration]

    return fulfillment

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item in fulfillment_cart:
        if item  in store_inventory:
            stock, aisle, refrigeration = store_inventory[item]
            order, _, _ = fulfillment_cart[item]
            if stock >= order:
                remaining = stock - order
                if remaining == 0:
                    store_inventory[item] = ['Out of Stock', aisle, refrigeration]
                else:
                    store_inventory[item] = [remaining, aisle, refrigeration]
            elif stock == 0:
                # Explicitly mark as out of stock
                store_inventory[item] = ['Out of Stock', aisle, refrigeration]
                
    return store_inventory
