# -*- coding: utf-8 -*-

# Numbers Strings Lists Tuples Dictionary



# + - * / % ** //

print("5 * 2 :", 5 ** 2)

# 单斜杠被除数和除数都是整数时不管结果是多少，结果都取整数，如果任意一个数是浮点数，结果比为真实值
# 双斜杠执行地板除，不管你是双精度还是浮点数除永远都是取最接近真实值得整数，
print("5 / 2 :", 5 / 2)
print("5.1 / 2 :", 5.1 / 2)
print("5 // 2 :", 5 // 2)
print("5.1 // 2 :", 5.1  // 2)

unique = "\" you are unique"

multiply_line = ''' multiply
line'''

print("%s,%s,%s" % (unique,multiply_line,"test"))

grocery_list = ["juic","tomatoes","potatoes"]
print(grocery_list)
grocery_list[0]="nothing"
print(grocery_list)
print(grocery_list[1:3])
# result:
# ['juic', 'tomatoes', 'potatoes']
# ['nothing', 'tomatoes', 'potatoes']
# ['tomatoes', 'potatoes']

other_events = ["1","2","3"]
to_do_list =[grocery_list,other_events]
print(to_do_list)
# result
# [['nothing', 'tomatoes', 'potatoes'], ['1', '2', '3']]

grocery_list.append("potatos")
print(grocery_list)
grocery_list.insert(1,"potatos")
print(grocery_list)
# remove first occurrence of value.
grocery_list.remove("potatos")
print(grocery_list)
del grocery_list[0]
print(grocery_list)
# result:
# ['nothing', 'tomatoes', 'potatoes', 'potatos']
# ['nothing', 'potatos', 'tomatoes', 'potatoes', 'potatos']
# ['nothing', 'tomatoes', 'potatoes', 'potatos']
# ['tomatoes', 'potatoes', 'potatos']

# http://sthurlow.com/python/lesson06/
# Tuples, Lists, and Dictionaries



