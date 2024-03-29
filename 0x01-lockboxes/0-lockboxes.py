#!/usr/bin/python3
""" This Module contains a function `canUnlockAll` """


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        for key in keys:
            if key >= 0 and key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
