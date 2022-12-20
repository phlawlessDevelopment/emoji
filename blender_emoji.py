# emoji,description,version,keywords,category,group,subgroup,parent,components

import csv
import json


def parse_csv(file_path):
    # define output dict
    result = {}

    # open file and read
    with open(file_path, mode="r") as f:
        reader = csv.reader(f)
        
        # iterate over rows
        for i, row in enumerate(reader):
            
            # skip header row
            if i < 1:
                continue
            
            # get all useful data
            emoji = row[0]
            keywords = row[3].split("|")
            descriptions = row[2].split(" ")

            # make lists even though these are 1 item
            categories = [row[4]]
            groups = [row[5]]
            subgroups = [row[6]]
            
            # concat all lists and deduplicate
            keys = set(keywords + descriptions + categories + groups + subgroups)
            
            # fill result dict
            for key in keys:
                key = key.lower()
                if key in result:
                    # append to existing list
                    result[key].append(emoji)
                else:
                    # create new list
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


json_data = load_from_json("emoji.json")


'''
this doesn't work yet, but it should be something like this
'''

input_gameobject = {} # todo: get this from blender , should be a single object
output_gameobjects = [] # todo: get this from blender, should be a list of objects

emojis = json_data.get(input_gameobject['input_prop'])

if emojis is not None:
    for i, emoji in enumerate(emojis):
        output_gameobjects[i]['output_prop'] = emoji



# while True:
#     key = input("type something -> ")
#     if key in json_data:
#         print(key)
#         print(json_data[key])
#         # for emoji in json_data[key]:
#         #     print(emoji)
#     else:
#         print(f"{key} - not found")
