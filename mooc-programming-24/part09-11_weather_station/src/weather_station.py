# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        if name != '':
            self.__name = name
            self.__entries = []
        else:
            raise ValueError('Name can\'t be an empty string')
    
    def __str__(self):
        return f"{self.__name}, {len(self.__entries)} observations"

    # @property
    # def name(self):
    #     return self.__name

    # @name.setter
    # def name(self, name: str):
    #     if name != '':
    #         self.__name = name
    #     else:
    #         raise ValueError('Name can\'t be an empty string')

    def add_observation(self, observation: str):
        if observation != '':
            self.__entries.append(observation)
        else:
            raise ValueError('The entry can\'t be an empty string')
    
    def latest_observation(self):
        if len(self.__entries) > 0:
            return self.__entries[-1]
        return ''
    
    def number_of_observations(self):
        return len(self.__entries)

if __name__ == '__main__':
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)