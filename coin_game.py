from random import randint


class Coin():
    """Defines the two-sided fair coin."""
    def __init__(self):
        self.state = None

    def __str__(self):
        return self.state

    def get_coin_state(self):
        return self.state

    def flip_coin(self):
        state = randint(0, 1)
        if state == 1:
            return 'heads'
        else:
            return 'tails'


class Player():
    """Defines a Player in the coin flip game."""
    def __init__(self, name):
        self.name = name
        self._coin_choice = ''

    def __str__(self):
        return self.name

    def choose_coin(self):
        coin_choice = input("Hello, " + self.name + "! Choose heads or tails: ").lower().strip()
        self._coin_choice = coin_choice
        return coin_choice

    def get_coin_choice(self):
        return self._coin_choice

    def set_coin_choice(self, coin_choice):
        self._coin_choice = coin_choice

    def has_won(self, winning_coin_choice):
        return self._coin_choice == winning_coin_choice


class CoinGame():
    """Defines an iteration of the coin toss game."""
    def __init__(self, players):
        self.players = players
        self.player_one = Player(self.players[0])
        self.player_two = Player(self.players[1])
        self.coin = Coin()

    def choose_first_player(self):
        return randint(0, 1)

    def start_game(self):
        if self.choose_first_player() == 0:
            print(self.player_one.name + " will choose the coin side.")
            first_player = self.player_one
            second_player = self.player_two
        else:
            print(self.player_two.name + " will choose the coin side.")
            first_player = self.player_two
            second_player = self.player_one

        random_coin = self.coin.flip_coin()     
        first_coin_choice = first_player.choose_coin()
        print("The winner is {}.".format(random_coin))

        if first_coin_choice == 'heads':
            second_player_choice = second_player.set_coin_choice('tails')
        else:
            second_player_choice = second_player.set_coin_choice('heads')

        print("Player one wins? " + str(first_player.has_won(random_coin)))
        print("Player two wins? " + str(second_player.has_won(random_coin)))


if __name__ == '__main__':
    game = CoinGame(['james', 'jeff'])
    print(game.start_game())
