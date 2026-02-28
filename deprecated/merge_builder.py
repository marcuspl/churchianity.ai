import os

drafts = [
    "draft_part1.md",
    "draft_part2.md",
    "draft_part3.md"
]

final_draft = "/home/marcus/code/new/writings/the-gap/merged-draft.md"

with open(final_draft, "a") as out_file:
    for d in drafts:
        with open(d, "r") as in_file:
            out_file.write("\n")
            out_file.write(in_file.read())

for d in drafts:
    os.remove(d)
