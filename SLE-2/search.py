import time

# A graph representing a small maze layout (16 nodes total)
MAZE_GRAPH = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': ['K'],
    'G': ['L', 'M'],
    'H': [],
    'I': [],
    'J': ['N'],
    'K': [],
    'L': ['O'],
    'M': ['P'],
    'N': [],
    'O': [],
    'P': []
}

def profile_bfs(graph, start, target):
    node_count = 0
    visited = set()
    queue = [[start]]
    
    if start == target:
        return 1
        
    while queue:
        path = queue.pop(0)
        node = path[-1]
        node_count += 1
        
        if node == target:
            return node_count
            
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return node_count

def profile_dfs(graph, start, target):
    node_count = 0
    visited = set()
    stack = [[start]]
    
    while stack:
        path = stack.pop()
        node = path[-1]
        node_count += 1
        
        if node == target:
            return node_count
            
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return node_count

def run_scenario(graph, start, target, scenario_name, runs=1000):
    # Benchmark BFS
    start_time = time.perf_counter()
    for _ in range(runs):
        bfs_nodes = profile_bfs(graph, start, target)
    end_time = time.perf_counter()
    avg_bfs_time = ((end_time - start_time) / runs) * 1000

    # Benchmark DFS
    start_time = time.perf_counter()
    for _ in range(runs):
        dfs_nodes = profile_dfs(graph, start, target)
    end_time = time.perf_counter()
    avg_dfs_time = ((end_time - start_time) / runs) * 1000

    print(f"\n--- {scenario_name.upper()} CASE (Target: '{target}') ---")
    print(f"BFS Time: {avg_bfs_time:.5f} ms | Nodes Expanded: {bfs_nodes}")
    print(f"DFS Time: {avg_dfs_time:.5f} ms | Nodes Expanded: {dfs_nodes}")
    
    return avg_bfs_time, bfs_nodes, avg_dfs_time, dfs_nodes

def main():
    print("==================================================")
    print("      LAUNCHING COMPREHENSIVE CASE ANALYSIS")
    print("==================================================")
    
    # 1. Best Case: Target is near the root node
    run_scenario(MAZE_GRAPH, 'A', 'B', "Best")
    
    # 2. Average Case: Target is deep down the right branch
    run_scenario(MAZE_GRAPH, 'A', 'P', "Average")
    
    # 3. Worst Case: Target is non-existent (Full Traversal)
    run_scenario(MAZE_GRAPH, 'A', 'Z', "Worst")
    
    print("\n==================================================")

if __name__ == "__main__":
    main()
