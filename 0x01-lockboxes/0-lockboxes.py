#!/usr/bin/python3

from collections import deque

def canUnlockAll(boxes):
    # Create a list to track visited boxes; initialize all as False
    visited = [False] * len(boxes)
    # Create a queue to store boxes to be checked, start with box 0
    queue = deque([0])
    # Mark the first box as visited
    visited[0] = True

    # Start traversal
    while queue:
        current_box = queue.popleft()  # Take the first box from the queue
        # Check keys in the current box
        for key in boxes[current_box]:
            if not visited[key]:  # If the key can open an unvisited box
                visited[key] = True  # Mark the box as visited
                queue.append(key)  # Add the box to the queue for further checking

    # Check if all boxes have been visited
    return all(visited)

