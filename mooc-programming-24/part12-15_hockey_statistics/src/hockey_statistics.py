# Write your solution 
import json

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, 
        penalties: int, games: int, team: str):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals =  goals
        self.penalties = penalties
        self.games = games
        self.team = team

    def __str__(self):
        return f"{self.name:20} {self.team:4} \
{self.goals:2} + {self.assists:2} = {self.get_points():3}"

    def get_points(self):
        return self.goals + self.assists


class Team:
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.__players = {}

    def add_player(self, player: Player):
        self.__players[player.name] = player

    def all_players(self):
        players = self.__players
        return {player.name: player for player in sorted(players.values(), key=lambda x: x.get_points(), reverse=True)}

    def __str__(self):
        return f"{self.team_name}"

class SportStats:
    def __init__(self):
        self.__teams = {}

    def add_team(self, team: Team):
        self.__teams[team.team_name] = team

    def all_teams(self):
        return {k: v for k, v in sorted(self.__teams.items())}
    
    def all_players(self):
        players = {}
        for team in self.all_teams().values():
            players.update(team.all_players())
        return {player.name: player for player in sorted(players.values(), key=lambda x: x.get_points(), reverse=True)}

    def all_countries(self):
        players = self.all_players()
        countries = sorted(list(set([i.nationality for i in players.values()])))
        return countries

    def search_player(self, name: str):
        if name in self.all_players().keys():
            return self.all_players()[name]
        return None
    
    def search_team(self, team: str):
        if team in self.all_teams().keys():
            return self.all_teams()[team]
        return None

class FileHandler:
    def __init__(self, file: str):
        self.__file_name = file
    
    def load_file(self):
        with open(self.__file_name) as my_file:
            loaded = my_file.read()

        data = json.loads(loaded)
        return data


class SportStatsApp:
    def __init__(self):
        self.__hockeystats = SportStats()
    
    def fill_sport(self, data: list):
        for i in data:
            if i['team'] not in self.__hockeystats.all_teams().keys():
                self.__hockeystats.add_team( Team( i['team'] ) )
            team = self.__hockeystats.all_teams()[i['team']]
            player = Player( i['name'], i['nationality'], i['assists'], i['goals'], 
                i['penalties'], i['games'], i['team'] )
            team.add_player(player)
        print(f"read the data of {len(data)} players")

    def run(self):
        # file_name = input('file name: ')
        # file_name = 'partial.json'
        file_name = 'all.json'
        self.__filehandler = FileHandler(file_name)
        data = self.__filehandler.load_file()
        self.fill_sport( data )
        print()
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_player()
            elif command == "2":
                self.all_teams()
            elif command == "3":
                self.all_countries()
            elif command == "4":
                self.players_of_team()
            elif command == "5":
                self.players_of_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.help()
        
        # for name, team in self.__hockeystats.all_teams().items():
        #     print('****************************************')
        #     print(team)
        #     print('----------------------------------------')
        #     for names, player in team.all_players().items():
        #         print(player)

    def help(self):
        print('commands:')
        print('0 quit')
        print('1 search for player')
        print('2 teams')
        print('3 countries')
        print('4 players in team')
        print('5 players from country')
        print('6 most points')
        print('7 most goals')

    def search_player(self):
        name = input('name: ')
        player = self.__hockeystats.search_player(name)
        print()
        print(player) if player is not None else print('unknown player')

    def all_teams(self):
        teams = self.__hockeystats.all_teams().values()
        for team in teams:
            print(team)

    def all_countries(self):
        countries = self.__hockeystats.all_countries()
        for country in countries:
            print(country)

    def players_of_team(self):
        team_name = input('team: ')
        team = self.__hockeystats.search_team(team_name)
        print()
        if team is not None:
            for i in team.all_players().values():
                print(i)
        else:
            print('unknown team')

    def players_of_country(self):
        country = input('country: ')
        players = self.__hockeystats.all_players()
        print()
        for player in players.values():
            if player.nationality == country:
                print(player)
            # print(player)

    def most_points(self):
        try:
            num = int(input('how many: '))
            players = sorted(list( self.__hockeystats.all_players().values() ), key=lambda player: (player.get_points(), player.goals), reverse = True )
            print()
            for i in range(num):
                print(players[i])
        except:
            print('input invalid')
        
    def most_goals(self):
        try:
            num = int(input('how many: '))
            players = sorted(list( self.__hockeystats.all_players().values() ), key=lambda player: (player.goals, -player.games), reverse = True )
            print()
            for i in range(num):
                print(players[i])
        except:
            print('input invalid')


app = SportStatsApp()
app.run()

# for name, team in hockey.all_teams().items():
#     print('****************************************')
#     print(team)
#     print('----------------------------------------')
#     for names, player in team.all_players().items():
#         print(player)

        # for i in hockey.all_teams():
        #     print(i)
        #     for j in i.all_players():
        #         print(j)
        # print('End')
    
    # p1 = Player('Cristiano', 'SUD', 43, 67, 2, 60)

#     {
#       "name": "Travis Zajac",
#       "nationality": "CAN",
#       "assists": 16,
#       "goals": 9,
#       "penalties": 28,
#       "team": "NJD",
#       "games": 69
#     },

# t1 = Team("NJD")
# p1 = Player('Cristiano', 'SUD', 43, 67, 2, 60)
# p2 = Player('Ronaldo', 'AME', 1, 8, 32, 80)
# t1.add_player(p1)
# t1.add_player(p2)
# hockey.add_team(t1)

# for i in hockey.all_teams():
#     print(i)

#     for j in i.all_players():
#         print(j)




