print()
import json

fly: str = "src/school_tests/2.second_test/json-for-test-nov-25.json" 


with open(fly, encoding="utf-8") as fly_fil:
    fly_data: dict = json.load(fly_fil)
    

flyselskap = fly_data["flyselskap"]

print(f"{"Flyselvskap":^20}|{"Destinasjon":^20}|{"Avgang":^20}|")
print("----" * 16)

for fly in flyselskap:
    print(f"{fly["navn"]:^20}|{fly["avganger"][0]["destinasjon"]:^20}|{fly["avganger"][0]["tid"]:^20}|")
    print(f"{fly["navn"]:^20}|{fly["avganger"][1]["destinasjon"]:^20}|{fly["avganger"][1]["tid"]:^20}|")
    

