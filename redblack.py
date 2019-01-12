from bettingGame import BettingGame
from deck import Deck
from player import Player
from playerprovider import PlayerProvider


class RedBlack(BettingGame):
    """A betting game where if you draw red you win, black you lose."""

    def initializeGame(self):
        self.deck = Deck()
        self.gatherPlayers()

    def gatherPlayers(self):
        """This is a one person against the house game."""
        self.players = self.playerProvider.gatherPlayers(1)

    def runRound(self):
        self.deck.reset()

        for player in self.players:
            self.collectBet(player)

        card = self.deck.drawCard()
        print("The card was {card}".format(card=card))
        # if the card is red payout. (we have already taken from the bank)
        if card.suit in ['H', 'D']:
            for bet in self.roundBets:
                self.payBet(bet, 1)

    def __init__(self, playerprovider):
        BettingGame.__init__(self, playerprovider)
