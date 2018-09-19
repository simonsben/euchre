class team:
    def __init__(self, member_1, member_2):
        self.members = [member_1, member_2]
        self.points = 0
        self.tricks = []

    def add_trick(self, cards):
        self.tricks.append(cards)

    def clear_tricks(self):
        self.tricks = []

    def count_tricks(self):
        return len(self.tricks)
