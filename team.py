# Class to define team
class team:
    def __init__(self, member_1, member_2):
        self.members = [member_1, member_2]
        self.points = 0
        self.tricks = []

    # Adds a trick when team wins one
    def add_trick(self, cards):
        self.tricks.append(cards)

    # Clears tricks (at the end of the round)
    def clear_tricks(self):
        self.tricks = []

    # Give number of tricks this hand
    def count_tricks(self):
        return len(self.tricks)

    def __str__(self):
        output = 'Team: \n'
        for player in self.members:
            output += player
