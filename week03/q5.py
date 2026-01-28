# Question 5 ----------------------------------------------
# Dictionary >> collection which is ordered** and changeable. No duplicate members.
# ** ordered as of python v3.7(?)

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print(f"Alice's number: {contacts['Alice']}")

contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana {contacts}")

contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob: {contacts}")
# The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")
print(f"All names: {contacts.keys()}")
print(f"All numbers: {contacts.values()}")
print(f"Total contacts: {len(contacts)}")

