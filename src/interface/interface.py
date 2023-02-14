def show_winners(results):
    for item in results:
        print(f"{item['place']}. {item['first_name']} {item['last_name']} {item['prize']}")


def format_prize(prize):
    if prize is None:
        return ''

    return f"Price: {prize}"
