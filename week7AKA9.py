from collections import deque

class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

    def isNotEmpty(self):
        return len(self.items) > 0


class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        self.children = []

    def __repr__(self):
        return f"TreeNode('{self.contents}')"

    def addChildren(self, *contents):
        children = [TreeNode(c) for c in contents]
        self.children.extend(children)
        return children

    def bfs_badqueue(self):
        queue = Queue()
        queue.add(self)
        result = []
        
        while queue.isNotEmpty():
            node = queue.remove()
            result.append(node.contents)
            for child in node.children:
                queue.add(child)
        
        return result

    def bfs_deque(self):
        queue = deque([self])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node.contents)
            queue.extend(node.children)
        
        return result

    def dfs_deque(self):
        stack = deque([self])
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.contents)
            stack.extend(reversed(node.children))
        
        return result

# Tree Structure
root1 = TreeNode("Z")
[Q, R, S] = root1.addChildren("Q", "R", "S")
[A, B, C] = Q.addChildren("A", "B", "C")
[D, E] = R.addChildren("D", "E")
[F, G, H] = S.addChildren("F", "G", "H")
[T, U] = A.addChildren("T", "U")
[W] = D.addChildren("W")
[X, Y] = G.addChildren("X", "Y")
[J] = W.addChildren("J")

correct_dfs = "Z Q A T U B C R D W J E S F G X Y H".split(" ")
correct_bfs = "Z Q R S A B C D E F G H T U W X Y J".split(" ")

part1_ans = root1.bfs_badqueue()
print("\npart 1 goal:   ", correct_bfs)
if part1_ans == correct_bfs:
    print("part 1 successful match")
else:
    print("part 1 actual: ", part1_ans)

part2_ans = root1.bfs_deque()
print("\npart 2 goal:   ", correct_bfs)
if part2_ans == correct_bfs:
    print("part 2 successful match")
else:
    print("part 2 actual: ", part2_ans)

part3_ans = root1.dfs_deque()
print("\npart 3 goal:   ", correct_dfs)
if part3_ans == correct_dfs:
    print("part 3 successful match")
else:
    print("part 3 actual: ", part3_ans)
