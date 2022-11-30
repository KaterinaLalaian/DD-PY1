import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:  # TODO реализовать конвертер из csv в json
        list_ = [line_.rstrip() for line_ in f]
        list_of_lists = [line + new_line for line in list_]
        dict_in_list = []
        for value in list_of_lists:
            dict_ = {list_of_lists[e]: value[e] for e in range(len(list_of_lists))}
            dict_in_list.append(dict_)
    return dict_in_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
