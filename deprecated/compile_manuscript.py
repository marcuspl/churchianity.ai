import os
input_dir = "/home/marcus/code/new/writings/the-gap/manuscript-gemini"
output_file = "/home/marcus/code/new/writings/the-gap/manuscript-gemini.md"
files = [
    "00_Introduction.md",
    "01_Chapter_1.md",
    "02_Chapter_2.md",
    "03_Chapter_3.md",
    "04_Chapter_4.md",
    "05_Chapter_5.md",
    "06_Chapter_6.md",
    "07_Chapter_7.md",
    "08_Chapter_8.md",
    "09_Chapter_9.md",
    "10_Conclusion.md"
]
with open(output_file, "w") as out:
    out.write("# Continuity, Freedom, and the Places We Lost Each Other\n")
    out.write("*Full Manuscript Draft — Gemini 3.1 Pro*\n\n")
    out.write("---\n\n")
    for filename in files:
        filepath = os.path.join(input_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                out.write(f.read())
                out.write("\n\n---\n\n")
