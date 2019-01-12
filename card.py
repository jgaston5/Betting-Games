class Card:
    def __init__(self, value, suit):
        """Initializes a card.

        Keyword arguments:
        value -- the value of the card, valid values are 2, 3, 4, 5, 6, 7, 8, 9,10, 'J', 'Q', 'K', 'A'. Invalid values will default to 2.
        suit -- the suit of the card, valid values are 'H', 'D', 'S', 'C'. Invalid values will default to 'H'
        """
        if suit not in ['H', 'D', 'S', 'C']:
            suit = 'H'
        if value not in ['J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            value = '2'
        self.value = value
        self.suit = suit

    def __str__(self):
        return '{value}{suit}'.format(value=self.value, suit=self.suit)
