class Lottery(object):
    @staticmethod
    def get_winners(drown_participants, prizes=[]):
        winners = []
        for index, item in enumerate(drown_participants):
            winners.append(Lottery.get_winner_list(item, index, prizes))
        return winners

    @staticmethod
    def get_winner_list(item, index, prizes):
        return {"place": index + 1, "first_name": item.first_name, "last_name": item.last_name,
                "prize": Lottery.get_prize(index, prizes)}

    @staticmethod
    def get_prize(index, prizes):
        if index >= len(prizes):
            return ''

        return prizes[index]['name']
