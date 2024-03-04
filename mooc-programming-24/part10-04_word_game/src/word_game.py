# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        if len(player1_word) < len(player2_word):
            return 2
        return 1.5


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels1 = sum ( [player1_word.lower().count(i) for i in 'aeiou'] )
        vowels2 = sum ( [player2_word.lower().count(i) for i in 'aeiou'] )
        if vowels1 > vowels2:
            return 1
        if vowels1 < vowels2:
            return 2
        return 1.5


class RockPaperScissors(WordGame):
    options = ['rock', 'paper' , 'scissors']

    def __init__(self, rounds: int):
            super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        str1 = player1_word.lower()
        str2 = player2_word.lower()
        if str1 not in RockPaperScissors.options and str2 not in RockPaperScissors.options:
            return 1.5
        if str1 not in RockPaperScissors.options:
            return 2
        if str2 not in RockPaperScissors.options:
            return 1
        
        if str1 == str2:
            return 1.5
        
        if str1 == 'rock':
            winner = 1 if str2 == 'scissors' else 2
        elif str1 == 'paper':
            winner = 1 if str2 == 'rock'else 2
        elif str1 == 'scissors':
            winner = 1 if str2 == 'paper' else 2
        return winner

if __name__ == '__main__':
    ## Part 1
    # p = LongestWord(3)
    # p.play()

    ## Part 2
    # p = MostVowels(3)
    # p.play()

    ## Part 3
    p = RockPaperScissors(4)
    p.play()
