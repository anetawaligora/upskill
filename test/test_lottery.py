from lottery.lottery import Lottery
from participants.participant import Participant


class TestLottery:
    def test_get_winners_before_draw(self):
        lottery = Lottery(draw_counter=1, with_weights=True, participants=[], prizes=[])
        assert len(lottery.get_winners()) == 0

    def prepare_participants(self):
        participants = [Participant(participant_id=1, first_name="Aneta", last_name="X"),
                        Participant(participant_id=1, first_name="Aneta 2", last_name="X")]

        return participants
