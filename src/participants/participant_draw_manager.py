import sys
from random import choices

sys.path.append("..")


class ParticipantDrawManager(object):

    @staticmethod
    def draw_without_weights(participants, draw_counter):
        return choices(participants, k=draw_counter)

    @staticmethod
    def draw_with_weights(participants, draw_counter):
        weights = [int(participant.weight) for participant in participants]
        return choices(participants, k=draw_counter, weights=weights)

    @staticmethod
    def draw(participants, draw_counter, with_weights=False):
        if with_weights:
            return ParticipantDrawManager.draw_with_weights(participants, draw_counter)
        else:
            return ParticipantDrawManager.draw_without_weights(participants, draw_counter)
