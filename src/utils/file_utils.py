import json
from pathlib import Path


def get_participants_file_path(file):
    return Path.joinpath(Path().absolute(), 'src/data/inputs', file)


def as_json(results):
    return json.dumps({"results": results}, indent=4)
