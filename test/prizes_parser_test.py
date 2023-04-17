import sys
import unittest

sys.path.append("../src")

from prizes.prizes_parser import PrizeParser


class PrizesParserTest(unittest.TestCase):
    def test_parse_prize_template_with_specified_template_name(self):
        with PrizeParser('separate_prizes.json', 'test_data/lottery_templates') as prizes:
            self.assertEqual(len(prizes), 3)
            self.assert_prize(prizes[0], 'Gold medal')
            self.assert_prize(prizes[1], 'Silver medal')
            self.assert_prize(prizes[2], 'Bronze medal')

    def test_parse_prize_template_without_specified_template_name(self):
        with PrizeParser(None, 'test_data/lottery_templates') as prizes:
            self.assertEqual(len(prizes), 5)
            self.assert_prize(prizes[0], 'Annual Vim subscription')
            self.assert_prize(prizes[1], 'Annual Vim subscription')
            self.assert_prize(prizes[2], 'Annual Vim subscription')
            self.assert_prize(prizes[3], 'Annual Vim subscription')
            self.assert_prize(prizes[4], 'Annual Vim subscription')

    def assert_prize(self, prize, name):
        self.assertEqual(prize.name, name)


if __name__ == '__main__':
    unittest.main()
