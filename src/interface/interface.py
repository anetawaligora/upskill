def show_winners(drawings, file_path, prizes=[]):
    if file_path.name.endswith('.json'):
        show_winners_list_from_json(drawings, prizes)
    elif file_path.name.endswith('.csv'):
        show_winners_list_from_csv(drawings, prizes)


def show_winners_list_from_csv(drawings, prizes):
    for index, item in enumerate(drawings):
        print(f"{index + 1}. {item[1]} {item[2]} {get_prize(index, prizes)}")


def show_winners_list_from_json(drawings, prizes):
    for index, item in enumerate(drawings):
        print(f"{index + 1}. {item['first_name']} {item['last_name']} {get_prize(index, prizes)}")


def get_prize(index, prizes):
    if index >= len(prizes):
        return ''

    return f"Price: {prizes[index]['name']}"
