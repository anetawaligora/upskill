import sys
import unittest

sys.path.append("../src")

from participants.participant_parser import ParticipantParser


class ParticipantParserTest(unittest.TestCase):
    def test_parse_json_file_without_weights(self):
        with ParticipantParser('test_data/inputs/participants1.json', False, 'json') as participants:
            self.assertEqual(len(participants), 30)
            self.assert_first_participant(participants[0], 'Tanny', 'Bransgrove', 0)

    def test_parse_json_file_with_weights(self):
        with ParticipantParser('test_data/inputs/participants2.json', True, 'json') as participants:
            self.assertEqual(len(participants), 30)
            self.assert_first_participant(participants[0], 'Tanny', 'Bransgrove', 10)

    def test_parse_csv_file_without_weights(self):
        with ParticipantParser('test_data/inputs/participants1.csv', False, 'csv') as participants:
            self.assertEqual(len(participants), 30)
            self.assert_first_participant(participants[0], 'Tanny', 'Bransgrove', 0)

    def test_parse_csv_file_with_weights(self):
        with ParticipantParser('test_data/inputs/participants2.csv', True, 'csv') as participants:
            self.assertEqual(len(participants), 30)
            self.assert_first_participant(participants[0], 'Tanny', 'Bransgrove', 10)

    def assert_first_participant(self, participant, first_name, last_name, weight):
        self.assertEqual(participant.first_name, first_name)
        self.assertEqual(participant.last_name, last_name)
        self.assertEqual(participant.weight, weight)


if __name__ == '__main__':
    unittest.main()
