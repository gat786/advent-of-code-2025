# Algorithm for Part-1

1. In the first row check for `S` and immediately in the second row put a
`|` below it.
2. Do not do anything in the second row, Either do not do anything in the rows whose index are odd numbers because the action on them is taken from the rows which have even indexes.
3. In the even indexed rows from below that 
    i. For each element in row, if element right above it is `|` 
        a. If current element is a `^` then mark adjacent elements in its row as well as in the row below it as `|`, and increase the ray split count.
        b. If the current element is `.` then mark the current element as well as the element right below it as `|`.

# Algorithm for Part-2

1. Generate the tree using part1, store it as a resultant intermediate file.
2. From the intermediate result generate a graph.
3. Using the graph do and exhaustive travel to each node and save how many 
    child path it has.
4. After the completing calculating the path for leaf node, you can calculate 
    possible paths for the node above it.
5. Repeat the process until you reach the root node and have the total number 
    of paths.
