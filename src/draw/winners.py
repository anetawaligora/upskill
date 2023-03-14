def get_winners(drawings, file_path, prizes=[]):
    winners = []
    for index, item in enumerate(drawings):
        if file_path.name.endswith('.json'):
            winners.append(get_winner_list_from_json(item, index, prizes))
        elif file_path.name.endswith('.csv'):
            winners.append(get_winner_list_from_csv(item, index, prizes))
    return winners


def get_winner_list_from_csv(item, index, prizes):
    return {"place": index + 1, "first_name": item[1], "last_name": item[2],
            "prize": get_prize(index, prizes)}


def get_winner_list_from_json(item, index, prizes):
    return {"place": index + 1, "first_name": item['first_name'], "last_name": item['last_name'],
            "prize": get_prize(index, prizes)}


def get_prize(index, prizes):
    if index >= len(prizes):
        return ''

    return prizes[index]['name']
