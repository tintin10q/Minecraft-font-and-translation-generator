'''
Author: Quinten Cabo (tintin10q@hotmail.com, Quinten#4772)
A program that generates a default.json and a translations file from another smaller file
'''

from json import load, dumps
import copy
import re

class hex_chain():
    '''A class that generates a new hex value higher than the last one'''
    def __init__(self, h,increase=1):
        self.current_hex = hex(h)
        self.increase = increase
        print("Made hex chain starting from:",self.current_hex)

    def add_u(self,s):
        '''Adds $u to the begining of each hex that is returned the $ are later replaced with a '\' '''
        return r'$u' + s

    def generate_next_hex(self):
        '''Generate a hex code by converting the last hex to an int adding 1 and converting it back to an int'''
        return_value = int(self.current_hex,16)+self.increase
        return_value = str(hex(return_value))
        self.current_hex = copy.copy(return_value)
        return_value = self.add_u(return_value[2:].upper()) # remove 0x
        return return_value

# This is the starting unicode character
starting_hex = 0xE000

# Creating Class instance
unicode_chain = hex_chain(starting_hex)

# the backwards spaces font file is at the top
complete_data = {
    "providers": [
        {
            "type": "ttf",
            "file": "minecraft:negative_spaces.ttf",
            "shift": [0.0, 0.0],
            "size": 10.0,
            "oversample": 1.0
        }
    ]
}

loose_data = [] #  collects all the json that get's generated
translation_json = {} # collects all the tranlation strings
count = 0 # count's the amount of characters

# Read data
try:
    with open('generate_font_data.json') as f:
        data = load(f)
except FileNotFoundError:
    print("ERROR: 'generate_font_data.json' could not be found")
    input("Press enter to exit...")
    exit()

# Go trough data and create a font definition for every file name also create a translation for every file entry
for pack in data:
    for info in pack["file_names"]:
        count += 1
        uni_character = copy.deepcopy(pack) # Get all the information in for this character
        uni_character["file"] = uni_character["file"].replace("$", str(info))
        uni_character["chars"] = [unicode_chain.generate_next_hex()]
        uni_character.pop("file_names")
        loose_data.append(uni_character)
        tranlate_name = uni_character["file"]
        # Strip the name
        tranlate_name = re.sub(r".*:","",tranlate_name)
        tranlate_name = re.sub(r"\.png","",tranlate_name)
        tranlate_name = re.sub(r"/",".",tranlate_name)
        tranlate_name = str(tranlate_name)
        # Check if the name is in the json if it is in the json keep adding _ until it is not anymore in the json
        while tranlate_name in translation_json:
            tranlate_name = "_"+tranlate_name
        translation_json[tranlate_name] = str("".join(uni_character["chars"]))

# Get all the data in the providers list
for data in loose_data:
    complete_data["providers"].append(data)

# Write the output to default.json
with open('default.json', 'w+') as outfile:
    outfile.write(dumps(complete_data,indent=4))
    outfile.close()

# Write the output to en_us.json
with open('en_us.json', 'w+') as outfile:
    outfile.write(dumps(translation_json,indent=8))
    outfile.close()

print("default.json and en_us.json created with {} unicode characters".format(count))

# This because we have to deal with annoying \ escaping
file = open('default.json', 'r').read()
file = str(file)
new_file = re.sub(r"\$",r"\\",file) # Replace $ with \
open("default.json", "w").write(new_file)


file = open('en_us.json', 'r').read()
file = str(file)
new_file = re.sub(r"\$",r"\\",file) # Replace $ with \
open("en_us.json", "w").write(new_file)

input("Press enter to exit...")