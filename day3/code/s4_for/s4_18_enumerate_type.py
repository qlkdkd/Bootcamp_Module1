fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
    print(type(i), type(fruit))

print(type(enumerate(fruits)))