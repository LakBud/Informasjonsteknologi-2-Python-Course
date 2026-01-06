print()
import json

fly: str = "src/school_tests/2.second_test/json-for-test-nov-25.json" 

with open(fly, encoding="utf-8") as fly_fil:
    fly_data: dict = json.load(fly_fil)


alle_avganger = []
for fly in fly_data["flyselskap"]:
    for avgang in fly["avganger"]:
        alle_avganger.append({
            "tid": avgang["tid"],
            "navn": fly["navn"],
            "destinasjon": avgang["destinasjon"]
        })


alle_avganger.sort(key=lambda x: x["tid"])


print(f'{"Flyselskap":^20}|{"Destinasjon":^20}|{"Avgang":^20}|')
print("-" * 65)
for avgang in alle_avganger:
    print(f'{avgang["navn"]:^20}|{avgang["destinasjon"]:^20}|{avgang["tid"]:^20}|')
