# Fundamentals: They are four required fundamentals in any language. Those are called key points. 1. Terms, 2. Actions, 3. Data Types and 4. Best Practices.


# #Data Types
# 1. int (interger. use it for all numbers)
# 2. FloatingPointError
# 3. bool
# 4. Str (String. For all letters)
# 5. list
# 6. tuple
# 7. set
# 8. dict (dictionary)
# # A data type is a value in Python. 
# ##classes --custom data types
# ##Specialized data types (modules, something like extentions) 
# ## None - The absence of value.

#---

# ##Fundamentals of Data Type
# int and float
# print(type(6))
# print(type(2 - 4)) # substraction
# print(type(2 * 4)) # multiplication
# print(type(2 / 4)) # division 0.5

# print(2 ** 3) # exponents
# print(5 // 4) # fractions
# print(6 % 4) # percentages

# ###math functions
# print(round(3.9))
# ###abs absolute value. No negative number. For example:
# print(abs(-20))

# ---

#Floating numbers are like scientific notations. For example 300000000 * 0.00000015 can also be expressed as 3 * 10 ** 8 and 1.5 * 10 ** -7
# In this case the 3 gets multiplied by 1.5 = 4.5 and the exponents get substracted, 10 ** 8 - 10 ** -7 = 10 ** 1
# results: 4.5 * 10 ** 1 or 4.5 * 10 = 45

#---

#How human see mathematical numbers vs computers.
# US humans know 100 , 10 , and 1 , in fractions we know 1 / 10 , 1 / 100 and 1 / 1000, in decimals, we see it as 0.1 , 0.01 and 0.001. On the other hand computers see:
# 4 , 2 , and 1
# 1 /2 , 1 / 4 , 1 / 6 , 1 / 8 , 1 / 10

#---

# Operator precedence: for example: (20 + 3 * 4) 3 * 4 gets multiplied first, then 20 gets added to 12.
# print(20 - 3 * 4) 
# the result from the above equation is 8 because 3 * 4 gets multiplied first, the 12 gets substracted to 12.

# In Python the precendence order is as follow: 
# ()
# ** # power of
# print((20 - 3) + 2 ** 2) # results 21 because first, we solve the (), then solve the exponent (**). SO again, the precedence is as follow:
# ()
# **
# * /
# + -

# ---

