from redblack import RedBlack
from playerprovider import PlayerProvider
playerprovider = PlayerProvider()
game = RedBlack(playerprovider)


game.run()
