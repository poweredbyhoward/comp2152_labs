# Question 2 ----------------------------------------------
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

# count instances > count(element)
apples_in_cart = cart.count("apple")
print(f'Number of apples: {apples_in_cart}')

# get position > index(element)
index_of_milk = cart.index("milk")
print(f'Position of milk: {index_of_milk}')

# remove first instance of.. > remove(element)
cart.remove("apple")

# remove last item > pop(index) < default -1
last_item_removed = cart.pop()
print(f'Removed item using pop: {last_item_removed}')

# conditional 'element in list'
print(f'Is banana in cart? {"banana" in cart}')

print(f'Final cart: {cart}')