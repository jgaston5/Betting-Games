import math  # This allows us to use the floor function
import random
from card import Card


class Deck:
    values = ['J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10]
    suits = ['H', 'D', 'S', 'C']

    def __init__(self, numberOfDecks=1):
        """Initialize a deck of cards.

        Keyword arguments:
        numberOfDecks -- the number of decks of 52 controlled by this class. Only whole numbers greater than 1.
        """

        if numberOfDecks < 1:
            numberOfDecks = 1
        self.numberOfDecks = math.floor(numberOfDecks)
        self.reset()

    def reset(self):
        self.cards = []
        for counter in range(self.numberOfDecks):
            for suit in self.suits:
                for value in self.values:
                    self.cards.append(Card(value, suit))
        self.shuffle()

    def shuffle(self):
        """Shuffles the cards remaining in the deck."""
        random.shuffle(self.cards)

    def checkDeckCount(self):
        """Check the number of cards left in the deck."""
        return len(self.cards)

    def canDrawCards(self, numberOfCards):
        """Check if the desired number of cards can be drawn."""
        return len(self.cards) >= numberOfCards

    def drawCards(self, numberOfCards):
        """Draw the desired number of cards. Returns a list of Cards.

        An exception will be raised if an attempt is made to draw more cards than are left in the deck."
        """
        if numberOfCards > 1:
            result = []
            while len(result) < math.floor(numberOfCards):
                result.append(self.cards.pop())
            return result
        return [self.cards.pop()]

    def drawCard(self):
        """Draw a card. Returns either a Card.

        An exception will be raised if an attempt is made to draw more cards than are left in the deck."
        """
        return self.cards.pop()

    def __str__(self):
        return 'A {numberOfDecks} deck stack with {numberOfCards} left.'.format(numberOfDecks=self.numberOfDecks, numberOfCards=len(self.cards))
