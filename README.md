# Minecraft-font-and-translation-generator
A program that generates a default.json and a translations file (en_us.json) from another smaller file

How to use
-----------------------
Put your input in a file called "generate_font_data.json" this file should be in the same folder as the executable
There is an example "generate_font_data.json" included. Here are also 3 examples:
```json
[
  {
    "type": "bitmap",
    "file": "namespace:numbers/$.png",
    "name": "low_numbers.$",
    "ascent": -12,
    "height": 14,
    "file_names": [0,1,2,3,4,5,6,7,8,9]
  },
  {
    "type": "bitmap",
    "file": "namespace:numbers/$.png",
    "name": "numbers.$",
    "ascent": -12,
    "height": 14,
    "file_names": [0,1,2,3,4,5,6,7,8,9]
  },
  {
    "type": "bitmap",
    "file": "namespace:$.png",
    "name": "names.$",
    "ascent": -12,
    "height": 14,
    "file_names": ["Quinten","Cabo"]
  }
]
```
The program scans the json and creates a font with that setup for each item in file_names. 
The $ is replaced with the file name

"file": is the name of the image file
"name": is how the character will be named in the translation file

A new unicode is asigned for each font. The first unicode's is \uE001 you can change this in the 
.py version on line 30 

Running the example will make it way more clear then me trying to explain it

Negative spaces are included
-------------------
Negative spaces by AmberW#4615 are included with the generation and the translation file needed for
negative spaces is also included

