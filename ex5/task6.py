import random

class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        # Determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"Round {i}")
            answer1 = input("Player 1: ")
            answer2 = input("Player 2: ")

            winner = self.round_winner(answer1, answer2)
            if winner == 1:
                self.wins1 += 1
                print("Player 1 won")
            elif winner == 2:
                self.wins2 += 1
                print("Player 2 won")
            else:
                pass  # It's a tie

        print("Game over, wins:")
        print(f"Player 1: {self.wins1}")
        print(f"Player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0  # It's a tie
   
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        vowels = "ueoaiUEOAI"
        count1 = sum(1 for char in player1_word if char in vowels)
        count2 = sum(1 for char in player2_word if char in vowels)
        if count1 > count2:
            return 1
        elif count2 > count1:
            return 2
        else:
            return 0  # It's a tie        

class RockPaperScissorsLizardSpock(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        self.rules = {
            "scissors": ["paper", "lizard"],
            "paper": ["rock", "spock"],
            "rock": ["lizard", "scissors"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        if player1_word not in self.rules and player2_word not in self.rules:
            return 0  
        
        if player2_word in self.rules[player1_word] or player2_word not in self.rules:
            return 1 
        elif player1_word in self.rules[player2_word] or player1_word not in self.rules:
            return 2 
        else:
            return 0  # It's a tie         


# p=  WordGame(3) 
# p.play()

# game = LongestWord(3)
# game.play()

# game = MostVowels(3)
# game.play()

game = RockPaperScissorsLizardSpock(3)
game.play()