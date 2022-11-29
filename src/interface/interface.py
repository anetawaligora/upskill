from pathlib import Path


def initialize_drawings():
    input_files_directory = Path.joinpath(Path().absolute(), 'src/data/inputs')
    input_file_list = list(input_files_directory.iterdir())
    show_available_input_files(input_file_list)

    index_for_filename = input("Please provide index of file with data:")
    with_weights = input("Do exist weights in loaded file? y/n")
    draw_counter = int(input("How many times to make a draw?"))

    file_path = input_file_list[int(index_for_filename) - 1]
    print(f"Chosen file: {file_path}")

    return file_path, with_weights, draw_counter


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


def show_available_input_files(input_file_list):
    print('Please choose the index of available files:')

    for index, filepath in enumerate(input_file_list):
        print(f"({index + 1}) : {filepath.name}")


def get_prize(index, prizes):
    if index >= len(prizes):
        return ''

    return f"Price: {prizes[index]['name']}"
