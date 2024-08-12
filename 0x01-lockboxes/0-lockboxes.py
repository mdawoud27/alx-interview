#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes can be opened."""
    if boxes is None:
        return False

    total_boxes = len(boxes)
    unlocked = set()
    to_check = [0]

    while to_check:
        current_box = to_check.pop()

        if current_box not in unlocked:
            unlocked.add(current_box)

            for key in boxes[current_box]:
                if 0 <= key < total_boxes and key not in unlocked:
                    to_check.append(key)

    return len(unlocked) == total_boxes
