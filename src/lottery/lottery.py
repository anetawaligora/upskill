import sys
from random import choices

sys.path.append("..")


class Lottery(object):

    def __init__(self, participants, draw_counter, with_weights, prizes):
        self.participants = participants
        self.draw_counter = draw_counter
        self.with_weights = with_weights
        self.prizes = prizes
        self.drawn_participants = []

    def draw(self):
        if self.with_weights:
            weights = [int(participant.weight) for participant in self.participants]
            self.drawn_participants = choices(self.participants, k=self.draw_counter, weights=weights)
        else:
            self.drawn_participants = choices(self.participants, k=self.draw_counter)

    def get_winners(self):
        winners = []
        prizes_number = len(self.prizes)
        for index, item in enumerate(self.drawn_participants):
            winner = self.get_winner(item, index, prizes_number)
            winners.append(winner)
        return winners

    def get_winner(self, item, index, prizes_number):
        return {"place": index + 1, "first_name": item.first_name, "last_name": item.last_name,
                "prize": self.get_prize(index, prizes_number)}

    def get_prize(self, index, prizes_number) -> str:
        if index >= prizes_number:
            return ''

        return self.prizes[index].name
