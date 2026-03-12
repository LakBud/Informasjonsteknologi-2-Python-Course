with open("data/5/number.txt", encoding="utf-8") as file:
    for line in file:
        total = 0
        average = 0
        number_row = line.strip()
        numbers = number_row.split("-")

        for n in numbers:
            total += int(n)
        
        average = total / len(numbers)
        
        with open("data/5/new_number.txt", "a") as file:
            file.write(f"Number Row: {number_row} | Sum: {total} | Average: {average} \n")
