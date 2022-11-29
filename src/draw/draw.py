from random import choices


def draw_from_json(participants, draw_counter):
    return choices(participants, k=draw_counter)


def draw_from_json_weighted(participants, draw_counter):
    weights = [int(participant['weight']) for participant in participants]
    return choices(participants, k=draw_counter, weights=weights)


def draw_from_csv(participants, draw_counter):
    return choices(participants, k=draw_counter)


def draw_from_csv_weighted(participants, draw_counter):
    weights = [int(participant[3]) for participant in participants]
    return choices(participants, k=draw_counter, weights=weights)
