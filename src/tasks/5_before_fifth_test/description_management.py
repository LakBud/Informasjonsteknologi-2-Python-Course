# Which file
file_name = "data/5/description_data.txt"

while True:
    title = input("What is your name: ")
    description = input("Write your description: ")

    text = f"\n\nPERSON: -- {title:^2} --\nDESCRIPTION: {description}"

    with open(file_name, "a+") as file:
        file.write(text)

    again = input("Add another person? (y/n): ").lower()
    if again != "y":
        break