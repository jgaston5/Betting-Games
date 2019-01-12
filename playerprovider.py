import random
from player import Player


class PlayerProvider():
    """Class for Gathering players for betting games."""
    firstNames = ["John", "Jacob", "Jingle", "Heimer", "Smith"]
    lastNames = ["Anderson", "Jacobson", "Johnson", "Peterson"]

    def gatherPlayers(self, numberOfPlayers):
        players = []
        while len(players) < numberOfPlayers:
            random.shuffle(self.firstNames)
            random.shuffle(self.lastNames)
            players.append(
                Player(len(players), 250,
                       self.firstNames[0] + " " + self.lastNames[0]))

        return players
