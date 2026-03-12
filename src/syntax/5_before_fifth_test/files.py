
# ? Manual opening and closing of files

# We can open the data of a file by using open() and encode it to norwegian with utf-8
# file = open("data/5/text1.txt", encoding="utf-8")

# We can read what the data says by using read()
# print(file.read())

# We should close the file after its use is done
# file.close()


# ? Automatic opening and closing of files


# # With block is a try and finally block
# # the "as file" is an iterable which can be used in for loops
# with open("data/5/text1.txt", encoding="utf-8") as file:
#     # content = file.read() works the same too
#     content = ""
#     for line in file:
#         content += line

# print(content)

# ? Writing files using write()

# Which file
file_name = "data/5/writing_file.txt"

text = "coooooll"

# You need "w" (write) for it to write the whole file
# If you want to append text, use "a" (append) instead
# If you also want to read it then add a + to it
with open(file_name, "a+") as file:
    file.write(text)
    content_1 = file.read()

print(content_1)