# 4 types of build-in data types 
# 1. list
# 2. Tuple
# 3. Dictionary
# 4. set
stringVariable = "test String"
print(type(stringVariable))

fruitsList = ["apple", "pineapple", "mango"]
print(fruitsList)
print(type(fruitsList))

fruitsList1 = ["apple", "pineapple", "mango", "test"]
print(fruitsList1)
fruitsList1.remove("test")
print("after removed:", fruitsList1)