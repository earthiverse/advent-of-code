graph = {}
with open('day12_input.csv') as file:
    for line in file.readlines():
        datum = line.split("-")
        fromNode = datum[0]
        toNode = datum[1].rstrip()
        if fromNode not in graph:
            graph[fromNode] = []
        if toNode not in graph:
            graph[toNode] = []
        graph[fromNode].append(toNode)
        graph[toNode].append(fromNode)

print(graph)

numPaths = 0
def traverse(g, n, p):
    global numPaths
    if n == "end":
        numPaths += 1
        return

    for node in g[n]:
        # print("node is {}, {}".format(node, node.islower()))
        # print("p is {}".format(p))
        if node == "start":
            # Don't revisit start node
            continue
        if node.islower() and node in p:
            # Don't visit more than once
            # print("skipping")
            continue
        p2 = p.copy()
        p2.append(node)
        traverse(g, node, p2)

traverse(graph, "start", ["start"])
print(numPaths)

numPaths = 0
def traverse2(g, n, p):
    global numPaths
    if n == "end":
        # print(p)
        numPaths += 1
        return

    visited = {}
    visitedTwice = False
    for node in p:
        if node.islower():
            if node in visited:
                visitedTwice = True
                break
            else:
                visited[node] = True

    for node in g[n]:
        # print("node is {}, {}".format(node, node.islower()))
        # print("p is {}".format(p))
        if node == "start":
            # Don't revisit start node
            continue
        if node.islower() and visitedTwice and node in p:
            # Don't visit more than once
            # print("skipping")
            continue
        p2 = p.copy()
        p2.append(node)
        traverse2(g, node, p2)

traverse2(graph, "start", ["start"])
print(numPaths)