foodlist = ["milk", "soda", "cookies", "chips"]

print(foodlist[0])
print(foodlist[3])

#replace an item with a new item at the
# previous index position

foodlist.pop("cookies")
foodlist.insert("apple")
print("milk","soda","apple","chips")