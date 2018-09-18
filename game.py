from utilities import random_number, get_player

# Players are indexed from 0 to 3, going clockwise

class game:
    def __init__(self):
        dealer_id = random_number(4)
        self.dealer = dealer_id
        self.turn = get_player(dealer_id + 1)
