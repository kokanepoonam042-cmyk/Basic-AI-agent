
print("Name : Poonam Kokane")
print("25UAM027")

import time
from collections import deque

# ============================================================
# SLE-2: Empirical Performance Analysis
# BFS vs DFS
# ============================================================

NUM_NODES = 1200


def create_graph(num_nodes):
    """
    Create a simple connected graph with 1200 nodes.
    Each node is connected to the next node and,
    where possible, another nearby node.
    """
    graph = {i: [] for i in range(num_nodes)}

    for i in range(num_nodes - 1):
        graph[i].append(i + 1)

        if i + 2 < num_nodes:
            graph[i].append(i + 2)

    return graph


def bfs(graph, start, target):
    """
    Breadth-First Search.
    Returns the number of nodes expanded.
    """
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
    Depth-First Search.
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
    Measure one execution using perf_counter().
    Returns time in milliseconds and number of nodes expanded.
    """

    start_time = time.perf_counter()

    nodes_expanded = algorithm(graph, start, target)

    end_time = time.perf_counter()

    elapsed_ms = (end_time - start_time) * 1000

    return elapsed_ms, nodes_expanded


def run_experiment(graph, start, target, case_name, runs=3):

    bfs_times = []
    dfs_times = []

    bfs_nodes = []
    dfs_nodes = []

    print("\n" + "=" * 60)
    print(f"{case_name.upper()} CASE")
    print(f"Start Node : {start}")
    print(f"Target Node: {target}")
    print("=" * 60)

    for run in range(1, runs + 1):

        # ---------------- BFS ----------------
        bfs_time, bfs_count = measure_algorithm(
            bfs,
            graph,
            start,
            target
        )

        # ---------------- DFS ----------------
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

        print(f"\nRun {run}")
        print(f"BFS Time : {bfs_time:.5f} ms")
        print(f"DFS Time : {dfs_time:.5f} ms")
        print(f"BFS Nodes: {bfs_count}")
        print(f"DFS Nodes: {dfs_count}")

    # Calculate averages
    avg_bfs_time = sum(bfs_times) / runs
    avg_dfs_time = sum(dfs_times) / runs

    avg_bfs_nodes = sum(bfs_nodes) / runs
    avg_dfs_nodes = sum(dfs_nodes) / runs

    print("\n" + "-" * 60)
    print("AVERAGE")
    print("-" * 60)

    print(f"BFS Average Time : {avg_bfs_time:.5f} ms")
    print(f"DFS Average Time : {avg_dfs_time:.5f} ms")

    print(f"BFS Average Nodes: {avg_bfs_nodes:.2f}")
    print(f"DFS Average Nodes: {avg_dfs_nodes:.2f}")

    return {
        "case": case_name,
        "bfs_time": avg_bfs_time,
        "dfs_time": avg_dfs_time,
        "bfs_nodes": avg_bfs_nodes,
        "dfs_nodes": avg_dfs_nodes
    }


def main():

    print("=" * 60)
    print("SLE-2 EMPIRICAL PERFORMANCE ANALYSIS")
    print("BFS vs DFS")
    print("=" * 60)

    # Create 1200-node graph
    graph = create_graph(NUM_NODES)

    start_node = 0

    # --------------------------------------------------------
    # BEST CASE
    # Target is very close to the start
    # --------------------------------------------------------

    best_result = run_experiment(
        graph,
        start_node,
        1,
        "Best"
    )

    # --------------------------------------------------------
    # AVERAGE CASE
    # Target is somewhere in the middle
    # --------------------------------------------------------

    average_result = run_experiment(
        graph,
        start_node,
        600,
        "Average"
    )

    # --------------------------------------------------------
    # WORST CASE
    # Target does not exist
    # --------------------------------------------------------

    worst_result = run_experiment(
        graph,
        start_node,
        9999,
        "Worst"
    )

    # --------------------------------------------------------
    # FINAL SUMMARY
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    results = [
        best_result,
        average_result,
        worst_result
    ]

    print(
        f"{'Case':<12}"
        f"{'BFS(ms)':<15}"
        f"{'DFS(ms)':<15}"
        f"{'BFS Nodes':<15}"
        f"{'DFS Nodes':<15}"
    )

    print("-" * 70)

    for result in results:

        print(
            f"{result['case']:<12}"
            f"{result['bfs_time']:<15.5f}"
            f"{result['dfs_time']:<15.5f}"
            f"{result['bfs_nodes']:<15.2f}"
            f"{result['dfs_nodes']:<15.2f}"
        )

    print("=" * 70)


if __name__ == "__main__":
    main()