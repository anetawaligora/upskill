import sys

import pytest

sys.path.append("../src")

from participants.participant_parser import ParticipantParser


class TestParticipantParser:
    @pytest.mark.parametrize("participant_file_path,file_type,with_weights,weight",
                             [('test_data/inputs/participants1.json', "json", False, 0),
                              ('test_data/inputs/participants2.json', 'json', True, 10),
                              ('test_data/inputs/participants1.csv', 'csv', False, 0),
                              ('test_data/inputs/participants2.csv', 'csv', True, 10)
                              ])
    def test_parse_json_file(self, participant_file_path, file_type, with_weights, weight):
        with ParticipantParser(participant_file_path, with_weights, file_type) as participants:
            first_participant = participants[0]

            assert len(participants) == 30
            assert first_participant.first_name == 'Tanny'
            assert first_participant.last_name == 'Bransgrove'
            assert first_participant.weight == weight
