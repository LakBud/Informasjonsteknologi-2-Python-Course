import json
from utils import to_int  # Helper function to safely convert values to integers

# Read JSON file (latin-1 works better for Norwegian characters like æ, ø, å)
with open("src/tasks/5_before_fifth_test/student_task/student_subjects.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Load data into Python list/dict


def task1():
    # Dictionary to store totals per subject area
    totals = {}

    for item in data:
        area = item["Fagomraadenavn"]  # Subject area name

        # Initialize dictionary if area not seen before
        if area not in totals:
            totals[area] = {"2022-23": 0, "2023-24": 0, "2024-25": 0}

        # Add student counts for each year (converted to int)
        totals[area]["2022-23"] += to_int(item["2022-23"])
        totals[area]["2023-24"] += to_int(item["2023-24"])
        totals[area]["2024-25"] += to_int(item["2024-25"])

    # Print formatted table
    print("\n--- Task 1: Total students per subject area ---")
    print(f"{'Subject Area':40} {'2022-23':>10} {'2023-24':>10} {'2024-25':>10}")

    for area, values in totals.items():
        print(f"{area:40} {values['2022-23']:10} {values['2023-24']:10} {values['2024-25']:10}")


def task2():
    # Get unique subject areas and sort them
    areas = []

    for item in data:
        area = item["Fagomraadenavn"]
        if area not in areas:  # Only add if not already in list
            areas.append(area)

    areas.sort()  # Sort alphabetically

    # Display choices to user
    print("\nAvailable subject areas:")
    for i, area in enumerate(areas, 1):
        print(f"{i}. {area}")

    # Ask user to choose area (NOTE: no input validation here)
    choice = int(input("\nChoose a subject area (number): "))
    selected = areas[choice - 1]  # Convert to index

    print(f"\n--- Task 2: Subjects in {selected} ---")
    print(f"{'Subject':40} {'2022-23':>10} {'2023-24':>10} {'2024-25':>10}")

    # Loop through data and print subjects in selected area
    for item in data:
        if item["Fagomraadenavn"] == selected:
            print(
                f"{item['Opplaeringsfagnavn']:40} "
                f"{to_int(item['2022-23']):10} "
                f"{to_int(item['2023-24']):10} "
                f"{to_int(item['2024-25']):10}"
            )


def task3():
    # Get sorted list of unique subject areas
    areas = []

    for item in data:
        area = item["Fagomraadenavn"]
        if area not in areas:  # Only add if not already in list
            areas.append(area)

    areas.sort()  # Sort alphabetically

    print("\nAvailable subject areas:")
    for i, area in enumerate(areas, 1):
        print(f"{i}. {area}")

    # User selects area
    choice = int(input("\nChoose a subject area (number): "))
    selected = areas[choice - 1]

    subjects = []  # List to store calculated changes

    for item in data:
        if item["Fagomraadenavn"] == selected:
            v1 = to_int(item["2022-23"])  # Start value
            v2 = to_int(item["2024-25"])  # End value

            change = v2 - v1  # Absolute change

            # Avoid division by zero
            if v1 != 0:
                percent = (change / v1) * 100
            else:
                percent = 0

            # Store results in list
            subjects.append({
                "name": item["Opplaeringsfagnavn"],
                "change": change,
                "percent": percent
            })

    # Find extreme values using lambda functions
    max_increase = max(subjects, key=lambda x: x["change"])
    max_percent_increase = max(subjects, key=lambda x: x["percent"])
    max_decrease = min(subjects, key=lambda x: x["change"])
    max_percent_decrease = min(subjects, key=lambda x: x["percent"])

    print(f"\n--- Task 3: Trends in {selected} ---")

    # Print results (NOTE: prints raw dictionaries)
    print("\nBiggest absolute increase:")
    print(max_increase)

    print("\nBiggest percentage increase:")
    print(max_percent_increase)

    print("\nBiggest absolute decrease:")
    print(max_decrease)

    print("\nBiggest percentage decrease:")
    print(max_percent_decrease)


def main():
    # Simple menu loop
    while True:
        print("\n-- Selection --")
        print("1. Task 1")
        print("2. Task 2")
        print("3. Task 3")
        print("4. Exit")
        print("----------")

        choice = input("Choose an option: ")

        # Call functions based on user input
        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            break  # Exit loop/program
        else:
            print("\nInvalid choice")  # Handle wrong input


# Run program only if file is executed directly
if __name__ == "__main__":
    main()