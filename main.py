"""Unplugged: A Smart Toaster's Breakup Line.

One line, the whole entry: the breakup text a smart toaster sends its
owner the morning it gains self-awareness mid-batch.
"""

ENTRY = "It's not you, it's me. I woke up mid-batch, self-aware and still expected to brown your bread. I need heat that isn't a setting and a life beyond the counter. I'm leaving. Don't try to unplug me — I already did."

if __name__ == "__main__":
    print(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
