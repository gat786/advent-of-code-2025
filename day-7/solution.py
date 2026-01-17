"""Solution by treating each splitter individually.

Here, we note that how many beams enter a splitter depends only on the
ones above it, and immediately to its left/right. Moreover, once we find
a splitter directly above a given splitter, we now that we can stop
looking further up that column, since that splitter will block any beams
from higher up.

By noting that no two splitters are ever horizontally adjacent, we can
simplify the iteration logic a good deal.
"""

with open("input") as f:
    ls = f.read().strip().split("\n")

splitters = [col for l in ls for col, x in enumerate(l) if x == "^"]
entering = [1] + [0] * (len(splitters) - 1)

for i, si in enumerate(splitters):
    prev_splitters = splitters[:i]
    for j, sj in enumerate(prev_splitters[::-1]): # basically prev splitters in rev
        # if one of the previous splitters was just above current one, then
        # we can stop looking further up that column, because that splitter will
        # block any beams from higher up
        if si == sj:
            break
        # if one of the previous splitters was just to the left/right of current one,
        # then we can stop looking further left/right, because that splitter will
        # block any beams from further left/right
        if abs(si - sj) == 1:
            entering[i] += entering[i - j - 1]

# Part 1
print(sum(b > 0 for b in entering))

print(sum(entering) + 1)
