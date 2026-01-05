print()
Tuple = (9, 2, 3, 4, 7) # * List with () instead of []


# for i in Tuple:
#     print(i)

# print(f"{Tuple[0]}\n")

# for i in range(len(Tuple)):
#     print(Tuple[0])

# ? Doesnt support editing its element at all.
# Tuple[0] = 1 
# Tuple.append(10)

# Tuple1 = ("Hello", "You")
# print(f"{Tuple1} is of {type(Tuple1)}")

# Tuple2 = "Hello", "You" # ? Does not need "()"
# print(f"{Tuple2} is of {type(Tuple2)}")

# Tuple1 = ("Hello", "World", "World")

# word1, word2, word3 = Tuple1 # ? You can define variables within tuple which is decided by the order (index) of it

# print(word1)
# print(word2)
# print(word3)

# -----------------------------
# # ? lists

# l = ["a", "b", "c"]

# b1, b2, b3 = l

# print(b1)
# print(b2)
# print(b3)

# print("------------------------")
# # ? String + Number

# s = "xyz"

# b1, b2, b3 = s

# print(b1)
# print(b2)
# print(b3)

# number = 1,2,3,4,5

# print(number) # ? Prints out the list with ()
# print("------------------------")

# print(*number) # ? Prints out the list without ()
# print("------------------------")

# print(*number, sep="\n") # ? Prints out the list with breaks and without ()

# ? You can combine lists and add new elements like 5 within it
# number1 = 1.2
# number2 = 3.4

# multiple_numbers = number1, number2, 5 

# print(multiple_numbers)
# print(*multiple_numbers, sep="\n")

# fruit1 = ["Apple", "Banana"]
# fruit2 = ["Pear", "Orange"]

# more_fruits = [fruit1, fruit2, "Pineapple"]

# for fruit in more_fruits:
#     print(fruit, end="\n")

# ? The *-operator can also be used to list different elements within one variable like c based on the order
# number = 1,2,3,4,5,6

# a,b,*c,d = number
# print(f"c is of type {type(c)}")
# print("------------------")
# print(a,b,c,d, sep="\n")

# ? The zip() function is an iterable & combines tuples and lists into one
# fruit = "apple", "banana", "orange"
# price = 10, 8, 12

# combined = zip(fruit, price)

# print(combined)
# print(*combined)
# print("--------------------")
# for fruit, price in zip(fruit, price):
#     print(f"The {fruit} costs {price} US dollars")


# ? We can convert a tuple into a list with the list() function
Tuple1 = (1, 2, 3, 4, "a", "b")
listy = list(Tuple1)
print(listy)

# ? We can convert a list into a tuple if the variable assigns with (*list,)
list = [1,2,3,4, "a", "b"]
tuply = (*list,)
print(tuply)
