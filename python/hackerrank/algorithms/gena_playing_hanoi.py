#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def disk_locations(posts):
    disks = [
        [
            i+1
            for i, P in enumerate(posts)
            if P == post
        ]
        for post in range(1, 4+1)
    ]
    return disks

def next_move(posts, disk, from_post, to_post):

    # def plus1(x):
    #     return x+1

    print(f"#  disk#{disk+1}: {from_post} -> {to_post}")
    if from_post == to_post:
        print("#    OK ALREADY")
        return None
    need_moved = [
        disk_i
        for disk_i, post_i in enumerate(posts)
        if post_i in [from_post, to_post] and disk_i < disk
    ]
    if not need_moved:
        return (disk, from_post, to_post)

    move_what = min(need_moved)
    print(f"#      (move {move_what+1} first)")
    to_where = [
        post_i
        for post_i in range(1, 4+1)
        if post_i not in [from_post, to_post]
    ]
    in_the_way = []
    for disk_i, post_i in enumerate(posts):
        if disk_i < move_what:
            if post_i in to_where:
                print(f"#   disk {disk_i+1} < {move_what+1}: not post {post_i}")
                to_where.remove(post_i)
                in_the_way.append((disk_i, post_i))
    print(f"#      {to_where=}")
    if len(to_where):
        empty_posts = [
            post_i
            for post_i in to_where
            if post_i not in posts
        ]
        print(f"#      {empty_posts=}")
        if empty_posts:
            to_where = empty_posts
        return next_move(posts, move_what, posts[move_what], to_where[0])
    print(f"#      {in_the_way=}")
    if len(in_the_way) != 2:
        raise Exception(f"#ERROR: nowhere to move {move_what+1}")
    in_the_way.sort()
    itw_from_tuple, itw_to_tuple = in_the_way
    itw_what, itw_from_where = itw_from_tuple
    itw_onto_what, itw_to_where = itw_to_tuple
    print(f"#      move {itw_what} first")
    return next_move(posts, itw_what, itw_from_where, itw_to_where)

# INT[] posts
# return INT
def hanoi(posts):
    moves = []
    print(f"#{posts=}")
    print(f"#{disk_locations(posts)=}")
    for disk in reversed(range(len(posts))):
        while True:
            post = posts[disk]
            move = next_move(posts, disk, post, 1)
            print(f"#      {move=}")
            if move is None:
                # already in proper location
                break
            
            moves.append(move)
            (next_disk, from_post, to_post) = move
            print(f"#BEFORE {posts} {disk_locations(posts)}")
            if posts[next_disk] != from_post:
                print(f"#ERROR: posts[{next_disk}]={posts[next_disk]} != {from_post}")
                assert posts[next_disk] == from_post
            posts[next_disk] = to_post
            print(f"# AFTER {posts} {disk_locations(posts)}")

    print(f"#{moves=}")
    print(f"#{posts=}")
    return len(moves)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    loc = list(map(int, input().rstrip().split()))
    res = hanoi(loc)
    print(str(res))
    # fptr.write(str(res) + '\n')
    # fptr.close()

