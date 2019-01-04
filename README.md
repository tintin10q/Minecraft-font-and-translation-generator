# Minecraft-font-and-translation-generator
A program that generates a default.json and a translations file (en_us.json) from another smaller file

How to use
-----------------------
Put your input in a file called "generate_font_data.json" this file should be in the same folder as the executable
There is an example "generate_font_data".json included
```json
[
  {
    "type": "bitmap",
    "file": "namespace:numbers/$.png",
    "ascent": -12,
    "height": 14,
    "file_names": [0,1,2,3,4,5,6,7,8,9
    ]
  },
  {
    "type": "bitmap",
    "file": "namespace:numbers/$.png",
    "ascent": -12,
    "height": 14,
    "file_names": [0,1,2,3,4,5,6,7,8,9]
  },
  {
    "type": "bitmap",
    "file": "namespace:$.png",
    "ascent": -12,
    "height": 14,
    "file_names": ["Quinten","Cabo"]
  }
]
```
The program scans the json and creates a font with that setup for each item in file_names.
The $ is replaced with the file name
Running the example will make way more clear then me trying to explain it

Negative spaces are included
-------------------
Negative spaces by AmberW#4615 are included with the generation and the translation file needed for
negative spaces is also included

