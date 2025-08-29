from rpsgame.player import HumanPlayer, ComputerPlayer
from rpsgame.game import Game


def main():
    player = HumanPlayer(name="Player")
    computer = ComputerPlayer(name="Computer")
    game = Game(player=player, computer=computer)
    game.play()


if __name__ == "__main__":
    main()
