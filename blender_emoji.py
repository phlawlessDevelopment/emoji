# emoji,description,version,keywords,category,group,subgroup,parent,components

import csv
import json


def parse_csv(file_path):
    result = {}
    with open(file_path, mode="r") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i < 1:
                continue
            emoji = row[0]
            keywords = row[3].split("|")
            descriptions = row[2].split(" ")
            categories = [row[4]]
            groups = [row[5]]
            subgroups = [row[6]]
            keys = set(keywords + descriptions + categories + groups + subgroups)
            for key in keys:
                if key in result:
                    result[key].append(emoji)
                else:
                    result[key] = [emoji]
    return result


def save_data_to_json(file_path, input_):
    with open(file_path, "w") as outfile:
        json.dump(input_, outfile)


# clean_data = parse_csv("emoji.csv")
# save_data_to_json("emoji.json", clean_data)


def load_from_json(file_path):
    with open(file_path, "r") as outfile:
        return json.load(outfile)


# json_data = load_from_json("emoji.json")


# while True:
#     key = input("type something -> ")
#     if key in json_data:
#         print(key)
#         print(json_data[key])
#         # for emoji in json_data[key]:
#         #     print(emoji)
#     else:
#         print(f"{key} - not found")
