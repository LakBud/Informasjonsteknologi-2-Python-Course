def retrieve_music_data(file_name: str) -> dict:
    years = []
    countries = []
    
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            parts = line.split()
            
            years.append(parts[0])
            countries.append(parts[1])
    
    # Create dictionary
    result = {
        "Year": years,
        "Country": countries
    }
    return result

print(retrieve_music_data("data/5/song_contest.txt"))