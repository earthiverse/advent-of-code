import sys

### WARNING:
### THIS CODE IS VERY INEFFICIENT!
### IT TAKES A VERY LONG TIME!


class Node:
    x = None
    y = None
    prev = None
    value = None

    def __init__(self, x, y, value, width):
        self.x = x
        self.y = y
        self.value = value
        self.width = width

    def __hash__(self):
        return int(self.y * self.width + self.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Node({},{},{})".format(self.x, self.y, self.value)


grid = []
ySize = 0
with open("day15_input.csv") as file:
    line = file.readline().strip()
    xSize = len(line)
    while line != "":
        gridLine = []
        for i in range(0, len(line)):
            gridLine.append(Node(i, ySize, int(line[i]), xSize))
        grid.append(gridLine)
        ySize += 1
        line = file.readline().strip()

# Pseudocode from http://www.gitta.info/Accessibiliti/en/html/Dijkstra_learningObject1.html
# 1: 	function Dijkstra(Graph, source):
def Dijkstra(graph, start, goal):
    # 2: 	for each vertex v in Graph: 	// Initialization
    for y in graph:
        for node in y:
            # 3: 	dist[v] := infinity 	// initial distance from source to vertex v is set to infinite
            node.dist = sys.maxsize
            # 4: 	previous[v] := undefined 	// Previous node in optimal path from source
            node.prev = None

    # 5: 	dist[source] := 0 	// Distance from source to source
    start.dist = start.value

    # 6: 	Q := the set of all nodes in Graph 	// all nodes in the graph are unoptimized - thus are in Q
    Q = set()
    for y in graph:
        for node in y:
            Q.add(node)

    # 7: 	while Q is not empty: 	// main loop
    while len(Q) != 0:
        # 8: 	u := node in Q with smallest dist[ ]
        lowestDist = sys.maxsize
        for node in Q:
            dist = node.dist
            if dist < lowestDist:
                lowestDist = dist
                u = node

        # 9: 	remove u from Q
        Q.remove(u)

        # 10: 	for each neighbor v of u: 	// where v has not yet been removed from Q.
        neighborNum = 0
        for y2 in range(u.y - 1, u.y + 2):
            for x2 in range(u.x - 1, u.x + 2):
                if x2 < 0 or x2 >= xSize or y2 < 0 or y2 >= ySize:
                    # Out of bounds
                    continue
                if x2 == u.x and y2 == u.y:
                    # Current Cell
                    continue
                if x2 != u.x and y2 != u.y:
                    # Diagonal Cell
                    continue

                v = graph[y2][x2]
                # 11: 	alt := dist[u] + dist_between(u, v)
                alt = u.dist + v.value

                neighborNum += 1

                # 12: 	if alt < dist[v] 	// Relax (u,v)
                if alt < v.dist:
                    # 13: 	dist[v] := alt
                    v.dist = alt
                    # 14: 	previous[v] := u
                    v.prev = u

    path = [goal]
    prev = goal.prev
    while prev is not None:
        path.append(prev)
        prev = prev.prev
    return path


# Compute the answer for part 1
path = Dijkstra(grid, grid[0][0], grid[ySize - 1][xSize - 1])
values = -grid[0][0].value
for link in path:
    values += link.value
print("Path cost: {}".format(values))

grid = []
ySize = 0
with open("day15_input.csv") as file:
    line = file.readline().strip()
    xSize = len(line) * 5
    while line != "":
        gridLine = []
        for i in range(0, len(line)):
            gridLine.append(Node(i, ySize, int(line[i]), xSize))
        grid.append(gridLine)
        ySize += 1
        line = file.readline().strip()

    # Expand x
    for y in range(0, len(grid)):
        gridLine = grid[y]
        for i in range(1, 5):
            for x in range(0, xSize // 5):
                value = gridLine[x].value + i
                if value > 9:
                    value -= 9
                gridLine.append(Node((xSize // 5) * i + x, y, value, xSize))

    # Expand y
    for i in range(1, 5):
        for y in range(0, ySize):
            gridLine = []
            for x in range(0, len(grid[y])):
                copyFrom = grid[y][x]
                value = copyFrom.value + i
                if value > 9:
                    value -= 9
                gridLine.append(Node(x, ySize * i + y, value, xSize))
            grid.append(gridLine)
    ySize *= 5


# print("Grid is {} x {}".format(xSize, ySize))

# for gridLine in grid:
#     for cell in gridLine:
#         print(cell.value, end="")
#     print()

# print("x check -----")
# for cell in grid[0]:
#     print(cell.x)

# print("y check -----")
# for gridLine in grid:
#     print(gridLine[0].y)

path = Dijkstra(grid, grid[0][0], grid[ySize - 1][xSize - 1])
# print(path)

values = -grid[0][0].value
for link in path:
    values += link.value
print("Path cost: {}".format(values))
