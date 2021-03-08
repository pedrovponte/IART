from State import *
from Utils import *
import time


def greedy(state: State, N: int):
    root = Node(state)
    stack = [root]
    tree = Tree(root)

    root.heuristics = h1(state.board) + h2(state.board)

    # list containing states (x,y) which were already discovered
    visited = []
    # keeping track of current tree depth
    depth = 1

    while depth != 1000 and len(stack) != 0:
        print("visited:", len(visited))
        stack.sort(key=lambda x: x.heuristics)

        s = stack.pop(0)
        depth = s.depth

        if flatten(s.info.board) not in visited:
            expanded = expand(s.info, N)
            # for each descendant we add the node to the tree and the new stack
            # we also create an edge between the parent and the newly created nod
            for x in expanded:
                new_node = Node(x)
                stack.append(new_node)
                tree.add_node(new_node)
                s.add_edge(new_node, 1)
            # as we already expanded 's' we need to add it's final state to the visited list
            visited.append(flatten(s.info.board))

        solution = contains_goal(stack, N)
        if solution is not None:
            print("Found Solution, Depth", depth)
            return solution, tree

    return None, tree


if __name__ == "__main__":
    print("---- GREEDY -----")

    print("8-PUZZLE")
    # board = [
    #     [8, 4, 6],
    #     [5, 0, 7],
    #     [2, 3, 1]
    # ]

    # initial = State(board, (1, 1), "Start")

    board = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    initial = State(board, (1, 1), "Start")
    print(initial)
    t = time.process_time()
    node, tree = greedy(initial, 8)
    print("Node: ", node)
    print("Tree: ", tree)
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
    elapsed_time = time.process_time() - t
    print("Elapsed Time:", elapsed_time)

    # print("15-PUZZLE")
    # board = [
    #     [15, 2, 1, 12],
    #     [8, 5, 6, 11],
    #     [4, 9, 10, 7],
    #     [3, 14, 13, 0]
    # ]
    # initial = State(board, (3, 3), "Start")
    # print(initial)

    # t = time.process_time()
    # node, tree = greedy(initial, 15)
    # if node is not None:
    #     path = find_path(node)
    #     print("- Solution -")
    #     print_path(path)
    # else:
    #     print("- No Solution -")
    # elapsed_time = time.process_time() - t
    # print("Elapsed Time:", elapsed_time)
