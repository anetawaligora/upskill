import sys
import unittest

sys.path.append("../src")

from lottery.lottery import Lottery
from participants.participant_parser import ParticipantParser
from prizes.prizes_parser import PrizeParser


class TestLottery(unittest.TestCase):

    def test_get_winners_before_draw(self):
        lottery = self.prepareLottery('separate_prizes.json', 5)

        winners = lottery.get_winners()

        self.assertEqual(len(winners), 0)

    def test_get_winners_after_draw(self):
        lottery = self.prepareLottery('separate_prizes.json', 5)

        lottery.draw()
        winners = lottery.get_winners()

        self.assertEqual(len(winners), 5)

    def test_only_three_winners_have_separate_prizes(self):
        lottery = self.prepareLottery('separate_prizes.json', 5)

        lottery.draw()
        winners = lottery.get_winners()

        self.assertEqual(len(winners), 5)
        self.assertEqual(winners[0]['prize'], 'Gold medal')
        self.assertEqual(winners[1]['prize'], 'Silver medal')
        self.assertEqual(winners[2]['prize'], 'Bronze medal')
        self.assertEqual(winners[3]['prize'], '')
        self.assertEqual(winners[4]['prize'], '')

    def test_five_first_winners_have_the_same_prize(self):
        lottery = self.prepareLottery('item_giveaway.json', 10)

        lottery.draw()
        winners = lottery.get_winners()

        self.assertEqual(len(winners), 10)
        self.assertEqual(winners[0]['prize'], 'Annual Vim subscription')
        self.assertEqual(winners[1]['prize'], 'Annual Vim subscription')
        self.assertEqual(winners[2]['prize'], 'Annual Vim subscription')
        self.assertEqual(winners[3]['prize'], 'Annual Vim subscription')
        self.assertEqual(winners[4]['prize'], 'Annual Vim subscription')
        self.assertEqual(winners[5]['prize'], '')
        self.assertEqual(winners[6]['prize'], '')
        self.assertEqual(winners[7]['prize'], '')
        self.assertEqual(winners[8]['prize'], '')
        self.assertEqual(winners[9]['prize'], '')

    def test_get_winners_after_draw_with_weights(self):
        lottery = self.prepareLottery('separate_prizes.json', 5, True)

        lottery.draw()
        winners = lottery.get_winners()

        self.assertEqual(len(winners), 5)

    def prepareParticipants(self, participant_file):
        with ParticipantParser(participant_file, False, 'json') as participants:
            return participants

    def preparePrizes(self, lottery_template_file):
        with PrizeParser(lottery_template_file, 'test_data/lottery_templates') as prizes:
            return prizes

    def prepareLottery(self, lottery_template_file, draw_counter, with_weights=False):
        participants_file = 'test_data/inputs/participants2.json' if with_weights \
            else 'test_data/inputs/participants1.json'
        participants = self.prepareParticipants(participants_file)
        prizes = self.preparePrizes(lottery_template_file)
        return Lottery(draw_counter=draw_counter, with_weights=with_weights, participants=participants, prizes=prizes)


if __name__ == '__main__':
    unittest.main()
