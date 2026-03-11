with open("data/5/description_data.txt", encoding="utf-8") as file:
    for line in file:
        print(line.strip()) # This strips any white space
        print(line.strip().strip("-")) # Does the same but with - as well
        
        # You can do the same with only one side with rstrip and lstrip

