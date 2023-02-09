# Set / Create
collection = db.collection('programmer_details')  # create collection
res = collection.document('A01').set({ # insert document
    'name': 'Vishnu',
    'age': 19,
    'Country': 'India',
    'Programming_languages': ['Python', 'C#', 'C++']
})
print(res)

# Get all rows
res = collection.get() # returns a list
for i in res: print(i.to_dict())

# convert to dict to use like json
res = collection.document('A01').get().to_dict()
print(res)

# update
res = collection.document('A01').update({
    'State': 'Chennai',
    'age': 21
})
