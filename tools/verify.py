import os
import yaml


def check_valid_file(file_info):
    pass


def get_valid_files():
    folder = "valid"
    return list(os.listdir(folder))


if __name__ == '__main__':
    with open("index.yaml") as f:
        catalogue = yaml.safe_load(f)
    valid_in_catalogue = {file['name'] for file in catalogue['files'] if file['valid']}

    valid_files = get_valid_files()

    for file in valid_files:
        assert file in valid_in_catalogue, "%s not present in the index" % (file, )

    for file in valid_in_catalogue:
        assert file in valid_files
        check_valid_file(file)
