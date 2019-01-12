from player import Player
from playerprovider import PlayerProvider


class BettingGame:
    """A base class for other games to inherit from.

    This handles collecting/paying out bets and running rounds.

    Base functionality:

    collectBet -- handles the interaction with a player to collect their bets.
    payBet -- pays the bet to the player. Takes in a decimal multiplier.


    Functions for implementers:
    initializeGame -- Perform any housekeeping required for the game -setting deck,gathering players etc. Called in initialization.
    runRound -- Run a round of the game. This will be called indefinetly until endGame() is called.
    """

    players = []

# Override Section

    def initializeGame(self):
        raise NotImplementedError("Method 'initializeGame' not implemented")

    def runRound(self):
        raise NotImplementedError("Method 'runRound' not implemented")


# Base Functionality


    def collectBet(self, player):
        amount = int(input("How much would you like to bet?"))
        self.roundBets.append(Bet(player, amount))
        print("{name} has wagered {amount}.".format(
            name=player.displayName, amount=amount))

    def payBet(self, bet, multiplier):
        # restore the bet amount, and the multiplier
        payout = bet.amount + (bet.amount * multiplier)
        bet.player.bank += payout
        print("{name} has won {amount}.".format(
            name=bet.player.displayName, amount=payout))

    def endGame(self):
        self.ended = True

    def run(self):
        print("Beginning game.")
        while self.ended != True:
            self.roundBets = []
            self.runRound()
        print("Thanks for playing.")

    def __init__(self, playerProvider):
        self.playerProvider = playerProvider
        self.ended = False
        self.initializeGame()


class Bet:

    def __init__(self, player, amount):
        self.player = player
        self.amount = amount
