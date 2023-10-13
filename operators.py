# Operators

'''
1. Arithmetic Operators -> Addition, Substraction, Mulitiplication, Division
2. String Operation -> Assignment, Concat, repetition, slicing, comparison, Membership, Escape sequence, Formating
3. Boolean Expression -> True, False
'''
# Boolean Expression
var1, var2 = 10, 5
print("Boolean ", var1 == var2)

# Arithmetic Operators
#Addition
addition = var1 + var2
print("Addition of var1 and var2 :", addition)

#substraction
sub = var1 - var2
print("Substraction of var1 and var2 :", sub)

#Multiplicaiton
mul = var1 * var2
print("Multiply of var1 and var2 :", mul)

#Divide
div = var1/var2
print("Divide of var1 and var2 :", div)

divWithQuotent = var1 // var2
print("Quotent value of div :", divWithQuotent)

divWithRound = round(div)
print("Round of div :", divWithRound)

print("Round of 0.3 :", round(0.3))
print("Round of 1.8 :", round(1.8))
print("Round of 1.4 :", round(1.4))

# String Operators
#Assignment Operator - "="
str1, str2 = "Hello", "All"
print("Assignment Operator :", str1, str2)

#Concatenate Operator - "+"
print("Concatenate Operator :", str1 + str2)

#Repetition Operator - "*"
print("Repetition Operator :", str2 * 3)
print("Repetition Operator :", str1 * 4)

# Comparison Operator - "==" or "!="
print("Comparison Operator :",str1 == str2)
print("Comparison Operator :", str1 != str2)

# Escape Sequence Operator - "\"
    # str3 = "Hello all happy "day"" -> it doesn't work
str3 = "Hello all happy \"day\""
print("Escape Sequece Operator :", str3)

# String Formatting Operator - "%" or "{}"
cName = "Toyoto"
model = 2022
price = 20.00
var1 = 'This is %s' % (cName)
print(var1)
var2 = 'The model is %d' % (model)
print(var2)
var3= 'This is %s, and the model is %d' % (cName, model)
print(var3)
var4= 'This %s, price is %f' % (cName, price)
print(var4)

# Slice Operator - "[]"
