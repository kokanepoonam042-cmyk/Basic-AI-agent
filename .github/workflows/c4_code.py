# SLE-3 - C4 Code Level
# Main functions of the BFS vs DFS Performance Analysis System


def create_graph(num_nodes):
    """
    Creates a connected graph with the specified number of nodes.
    Each node is connected to the next node and nearby node.
    """
    graph = {i: [] for i in range(num_nodes)}

    for i in range(num_nodes - 1):

        graph[i].append(i + 1)

        if i + 2 < num_nodes:
            graph[i].append(i + 2)

    return graph


def bfs(graph, start, target):
    """
    Performs Breadth First Search.
    Returns the number of nodes expanded.
    """
    from collections import deque

    node_count = 0
    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        node_count += 1

        if node == target:
            return node_count

        for neighbor in graph[node]:

            if neighbor not in visited:
                queue.append(neighbor)

    return node_count


def dfs(graph, start, target):
    """
    Performs Depth First Search.
    Returns the number of nodes expanded.
    """

    node_count = 0
    visited = set()
    stack = [start]

    while stack:

        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        node_count += 1

        if node == target:
            return node_count

        for neighbor in graph[node]:

            if neighbor not in visited:
                stack.append(neighbor)

    return node_count


def measure_algorithm(algorithm, graph, start, target):
    """
    Measures execution time and nodes expanded
    for one BFS or DFS execution.
    """
    import time

    start_time = time.perf_counter()

    nodes_expanded = algorithm(
        graph,
        start,
        target
    )

    end_time = time.perf_counter()

    elapsed_ms = (
        end_time - start_time
    ) * 1000

    return elapsed_ms, nodes_expanded


def run_experiment(graph, start, target, case_name, runs=3):
    """
    Runs an experiment multiple times and calculates
    average execution time and average nodes expanded.
    """

    bfs_times = []
    dfs_times = []

    bfs_nodes = []
    dfs_nodes = []

    for _ in range(runs):

        bfs_time, bfs_count = measure_algorithm(
            bfs,
            graph,
            start,
            target
        )

        dfs_time, dfs_count = measure_algorithm(
            dfs,
            graph,
            start,
            target
        )

        bfs_times.append(bfs_time)
        dfs_times.append(dfs_time)

        bfs_nodes.append(bfs_count)
        dfs_nodes.append(dfs_count)

    return {
        "case": case_name,
        "bfs_time": sum(bfs_times) / runs,
        "dfs_time": sum(dfs_times) / runs,
        "bfs_nodes": sum(bfs_nodes) / runs,
        "dfs_nodes": sum(dfs_nodes) / runs
    }


def main():
    """
    Controls graph creation, experiments and
    final performance summary.
    """

    NUM_NODES = 1200

    graph = create_graph(NUM_NODES)

    start_node = 0

    best_result = run_experiment(
        graph,
        start_node,
        1,
        "Best"
    )

    average_result = run_experiment(
        graph,
        start_node,
        600,
        "Average"
    )

    worst_result = run_experiment(
        graph,
        start_node,
        9999,
        "Worst"
    )

    results = [
        best_result,
        average_result,
        worst_result
    ]

    print("\nFINAL SUMMARY")

    for result in results:

        print(
            result["case"],
            result["bfs_time"],
            result["dfs_time"],
            result["bfs_nodes"],
            result["dfs_nodes"]
        )


if __name__ == "__main__":
    main()