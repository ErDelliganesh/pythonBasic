# case sensitive

a = 5
A = "sample text"

print(a)
print(A)

# comment

# single line comment
# This is the Comment


#multi-line comment
#Type 1
		# This
		# is 
		# the 
		# Comment

#Type 2 
''' This
	is
	the 
	comment'''

# Inline comment
length = width = height = 5
volume = length * width * height # volume of Rectangle -> This is Inline Comment
print(volume)


# Variable
'''
1. Use Alpha-Numeric Characters `(a-z, A-Z, 0-9)`
2. Use `_` for create Variable for better understanding
3. First character of variable name should not be Number
4. Key words are not considered as a variable
'''

_5x = "test" # _5x is variable here
print(_5x)

# Assign multiple variables to multiple value 
length, breath = 100, 200

print(length)
# 100

print(breath)
# 200

# Assign same value to multiple variables 
length = width = height = 5

'''value error if we doesn't follow the assigning values to the variable'''
# length, width, height = 5
# length, width, height = 5,5
# length, width, height = 5,5,5,5