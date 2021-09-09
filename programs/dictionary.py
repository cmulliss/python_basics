contacts = {"Mot": "01934", "Pengy": "05566"}

mots_phone = contacts["Mot"]
pengys_phone = contacts["Pengy"]

print("Dial %s to call Mot. " % (mots_phone))
print("Dial %s to call Pengy. " % (pengys_phone))

# add a contact to the dictionary
contacts["Me"] = 12345, 67898
print(contacts)
print(len(contacts))

for number in contacts["Mot"]:
    print("Phone number: %s" % (number))

# remove a contact from the dictionary
del contacts["Me"]
print(contacts)
