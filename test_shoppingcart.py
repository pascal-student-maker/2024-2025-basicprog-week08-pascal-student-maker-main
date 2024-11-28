from model.ShoppingCart import ShoppingCart

action_cart = ShoppingCart()
action_cart.add_product("cd1")
action_cart.add_product("cd2")
action_cart.add_product("cd3")
action_cart.add_product("cd4")
# action_cart.remove_product("cd5")     #<--- !

ikea_cart = ShoppingCart()
ikea_cart.add_product("Billy")
ikea_cart.add_product("Factum")

print(f"Shopping cart 1: {action_cart}\n")
print(f"Shopping cart 2: {ikea_cart}\n")


print("\n***** Shopping cart 3 = Shopping cart 1 + Shopping cart 2 *****")
christmas_cart = action_cart + ikea_cart
print(f"Shopping cart 3: {christmas_cart}")

print("\n***** Shopping cart 1 +=Shopping cart 2 *****")
action_cart += ikea_cart
print(f"Shopping cart 1: {action_cart}")
