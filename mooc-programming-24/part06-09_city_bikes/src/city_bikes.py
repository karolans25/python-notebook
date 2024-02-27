# Write your solution here
import math 

def get_station_data(filename: str):
    result = {}
    with open(filename) as new_file:
        for station in new_file:
            data = station.split(';')
            if data[3] == 'name':
                continue
            result[data[3]] = (float(data[0]), float(data[1]))
    return result

def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    start = ''
    end = ''
    greatest = 0

    for station1 in stations:
        for station2 in stations:
            dist = distance(stations, station1, station2)
            if dist > greatest:
                start = station1
                end = station2
                greatest = dist
    
    return start, end, greatest

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)