print()
import json
import tkinter as tk
from tkinter import font



root = tk.Tk()
root.title("Flytider")
root.geometry("600x600")

default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# ---------------------------------------------------------------------------------------------------------

fly: str = "src/school_tests/2.second_test/json-for-test-nov-25.json" 


with open(fly, encoding="utf-8") as fly_fil:
    fly_data: dict = json.load(fly_fil)

flyselskap = fly_data["flyselskap"]
sortert_flyselskap = sorted(flyselskap, key = lambda x: x["avganger"][0]["tid"])


# ---------------------------------------------------------------------------------------------------------

def choose_fly_details():
    if not fly_listbox.curselection():
        message.configure(text="Please select a flight")
        return
    
    chosen_fly = fly_listbox.curselection()
    selected_text = fly_listbox.get(chosen_fly)
    message.configure(text=f"Here are details about the {selected_text} flights:")
    
    details_content = ""
    
    for fly in sortert_flyselskap:
        if fly["navn"] == selected_text:
            for avganger in fly["avganger"]:
                details_content += "\n"
                for key, value in avganger.items():
                    details_content += f"{key:^25}{value:^25}\n"


    message_detail.configure(text=details_content)



# ---------------------------------------------------------------------------------------------------------

header = tk.Label(root, text="Flights for 24.12.2025") 
header.pack(pady=5)

fly_frame = tk.Frame(root)
fly_frame.pack(pady=20) 



fly_list_scroll = tk.Scrollbar(fly_frame, orient="vertical")
fly_listbox = tk.Listbox(fly_frame, height=5, width=15, yscrollcommand=fly_list_scroll.set)


for index, fly in enumerate(sortert_flyselskap):
    fly_listbox.insert(index, fly["navn"])


fly_listbox.pack(side="left", fill="both")
fly_list_scroll.configure(command=fly_listbox.yview)
fly_list_scroll.pack(side="right", fill="y")

button = tk.Button(root, text="Show Flight", command=choose_fly_details)
button.pack()

message = tk.Label(root, text="") 
message.pack(pady=5)

message_detail_frame = tk.Frame(root)
message_detail_frame.pack(pady = 20)

message_detail = tk.Label(message_detail_frame, text="")
message_detail.pack()


root.mainloop()
