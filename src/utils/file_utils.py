from pathlib import Path


def get_participants_file_path(file):
    return Path.joinpath(Path().absolute(), 'src/data/inputs', file)
