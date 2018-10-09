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

    # Give the team another point and check if team has won
    def hand_over(self, alone, caller):
        team_won = len(self.tricks) >= 3
        if not team_won:
            pass
        elif not caller in self.members:  # If team didn't call
            if len(self.tricks) >= 3:
                self.points += 2
        elif len(self.tricks) == 5:  # If team won all tricks
            if alone:
                self.points += 4
            else:
                self.points += 2
        elif len(self.tricks) >= 3:  # If team won (3 or 4 tricks)
            self.points += 1
        self.tricks = []

        return self.points >= 10, team_won

    # Check if player is on the team
    def is_on_team(self, player):
        return self.members.__contains__(player)

    def __str__(self):
        output = 'Team: \n'
        for player in self.members:
            output += player
