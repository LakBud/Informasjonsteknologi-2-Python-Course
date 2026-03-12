# CSV stands for Comma Separated Values

# How it looks like:
# 1;Sup! ;are
# 2;you ;cool?

# For csv file, we print out each line individually (supposed to look like a table)
with open("data/5/traffic_data.csv", encoding="utf-8") as file:
    content = ""
    for line in file:
        # The split() splits every element with comma into a list
        # The strip() strips out the selected element
        l = line.strip("\n").split(",")
        print(l)
        content += l[1] + l[2] + l[3] # If we wanted everything in one line. 

print()
print(content)