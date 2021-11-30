import math
import json
import os
import io
from datetime import datetime

box = "⬛"

colors = {
    "0": [0, 0, 0],
    # "1": [0, 0, 170],
    # "2": [0, 170, 0],
    # "3": [0, 170, 170],
    # "4": [170, 0, 0],
    # "5": [170, 0, 170],
    # "6": [255, 170, 0],
    # "7": [170, 170, 170],
    # "8": [85, 85, 85],
    # "9": [85, 85, 255],
    # "a": [85, 255, 85],
    # "b": [85, 255, 255],
    # "c": [255, 85, 85],
    # "d": [255, 85, 255],
    # "e": [255, 255, 85],
    "f": [255, 255, 255]
}


def formatnumber(num):
    return "{:0>7d}".format(num)


def src(num):
    return "frames/" + formatnumber(num) + ".raw"


def index(x, y, w):
    return (y * (w * 1)) + (x * 1)


def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in colors.values():
        cr, cg, cb = color
        color_diff = math.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


width = 40
height = 30

frames = len([name for name in os.listdir("frames/") if os.path.isfile(os.path.join("frames/", name))])

finished_frames = []
finished_framestrings = []
json_data = {}

print(f"Please wait. Converting frames: {str(frames)}")

start = datetime.now()

for i in range(1, frames + 1):
    f = open(src(int(i)), "rb")
    data = list(f.read())
    f.close()

    print(f"Frame {str(i)}")

    frame = []
    framestring = ""

    for y in range(0, height):
        line = ""
        for x in range(0, width):
            r = data[index(x, y, width)]
            g = data[index(x, y, width) + 1]
            b = data[index(x, y, width) + 2]

            for code, value in colors.items():
                if value == closest_color((r, g, b)):
                    line += f"\u00a7{code}{box}"
        frame.append(line)
        framestring += line

    finished_frames.append(frame)
    finished_framestrings.append(framestring)
    json_data[i] = frame

end = datetime.now()
print(f"Done! Running time: {str(end - start)}")

with io.open('output.json', 'w', encoding="utf-8") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)
    file.close()
