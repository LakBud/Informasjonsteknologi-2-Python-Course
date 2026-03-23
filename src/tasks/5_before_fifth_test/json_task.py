import json

file_name = "data/5/json-data1.json"

with open(file_name, encoding="utf-8") as file:
    data = json.load(file)
    
    print("People in the register:")
    people = data["personer"]
    
    for p in people:
        first_name = p["fornavn"]
        last_name = p["etternavn"]
        
        telephone_list = []
        
        for phone in p["telefon"]:
            telephone_list.append(phone["nummer"])
        
        print(f"{first_name} {last_name}: {', '.join(telephone_list)}")