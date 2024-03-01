# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rates = []
    
    def __str__(self):
        res = f"{self.title} ({self.seasons} seasons) \n"
        res += f"genres: {', '.join(self.genres)} \n"
        if len(self.rates) > 0:
            res += f"{len(self.rates)} ratings, average {self.get_rates_average():.1f} points"
        else:
            res += 'no ratings'
        return res

    def rate(self, rating: int):
        self.rates.append(rating)

    def get_rates_average(self):
        if len(self.rates) > 0:
            return round(sum(self.rates) / len(self.rates), 1)
        else:
            return 0.0

def minimum_grade(rating: float, series_list: list):
    return [i for i in series_list if rating < i.get_rates_average()] 

def includes_genre(genre: str, series_list: list):
    return [i for i in series_list if genre in i.genres] 


if __name__ == '__main__':
    ## Part 1
    # dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # print(dexter)

    ## Part 2
    # dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # dexter.rate(4)
    # dexter.rate(5)
    # dexter.rate(5)
    # dexter.rate(3)
    # dexter.rate(0)
    # print(dexter)

    ## Part 3
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
