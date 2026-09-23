#  Profiling Report
## Empirical Performance Analysis of BFS and DFS

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student Name:** Poonam Kokane  
**Student ID:** 25UAM027  
**Experiment:** Empirical Performance Analysis (BFS vs DFS)

---

### 1. Aim
The aim of this experiment is to experimentally compare the performance of Breadth First Search (BFS) and Depth First Search (DFS) on the same graph structure. 

The comparison evaluates their behavioral differences across **Best Case**, **Average Case**, and **Worst Case** scenarios based on execution time and the total number of nodes expanded by each search algorithm.

---

### 2. Algorithms Profiled
* **Breadth First Search (BFS):** Explores the graph layer by layer using a FIFO queue structure.
* **Depth First Search (DFS):** Explores a single path as deeply as possible before backtracking using a LIFO stack structure.

---

### 3. Problem Configuration
The experiment parses execution metrics across three distinctly tested graph exploration scenarios:
* **Best Case:** Start Node: 0 | Target Node: 1
* **Average Case:** Start Node: 0 | Target Node: 600
* **Worst Case:** Start Node: 0 | Target Node: 9999
* **Programming Language:** Python 3.14

---

### 4. Experimental Results

#### Scenario 1: Best Case (Target Node: 1)

| Run | BFS Time (ms) | DFS Time (ms) | BFS Nodes | DFS Nodes |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0.41840 | 0.30600 | 2 | 1200 |
| 2 | 0.00780 | 0.26370 | 2 | 1200 |
| 3 | 0.00570 | 0.25160 | 2 | 1200 |
| **Avg**| **0.14397** | **0.27377** | **2.00** | **1200.00** |

#### Scenario 2: Average Case (Target Node: 600)

| Run | BFS Time (ms) | DFS Time (ms) | BFS Nodes | DFS Nodes |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0.15050 | 0.06240 | 601 | 301 |
| 2 | 0.13870 | 0.05980 | 601 | 301 |
| 3 | 0.14400 | 0.06010 | 601 | 301 |
| **Avg**| **0.14440** | **0.06077** | **601.00** | **301.00** |

#### Scenario 3: Worst Case (Target Node: 9999)

| Run | BFS Time (ms) | DFS Time (ms) | BFS Nodes | DFS Nodes |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0.27520 | 0.22970 | 1200 | 1200 |
| 2 | 0.29280 | 0.22380 | 1200 | 1200 |
| 3 | 0.27490 | 0.22850 | 1200 | 1200 |
| **Avg**| **0.28097** | **0.22733** | **1200.00**| **1200.00**|

---

### 5. Final Summary Table

| Case | BFS (ms) | DFS (ms) | BFS Nodes | DFS Nodes |
| :--- | :---: | :---: | :---: | :---: |
| **Best** | 0.14397 | 0.27377 | 2.00 | 1200.00 |
| **Average** | 0.14440 | 0.06077 | 601.00 | 301.00 |
| **Worst** | 0.28097 | 0.22733 | 1200.00 | 1200.00 |

---

### 6. Observations & Structural Justification

* **Best Case Evaluation:** Since the target node (1) is located directly adjacent to the starting node, BFS finds it almost immediately, expanding only **2 nodes** with an optimal time of **0.14397 ms**. Conversely, DFS blindly traverses down its initial path, expanding **1200 nodes** before backtracking to find the target.
* **Average Case Evaluation:** In this specific graph structure layout, the target node (600) was situated in a manner that favored the deep traversal strategy of DFS, resulting in DFS expanding fewer nodes (**301 nodes**) and executing faster (**0.06077 ms**) compared to BFS (**601 nodes**).
* **Worst Case Evaluation:** When searching for node 9999, both algorithms hit their limits on this graph structure, forcing both to expand the maximum capacity of **1200 nodes**. 

---

### 7. AI Contribution
AI assistance was utilized to format benchmarking reports, organize layout readability, map terminal telemetry variables, and refine structural code implementation requirements. The student executed the Python environment profiles locally, managed runtime checks, captured terminal data streams, and updated repository branches.

---

### 8. Files in the Repository
* **`qq.py`** – Main Python script containing the BFS/DFS search variations, dataset loops, and evaluation execution limits.
* **`README.md`** – Empirical performance logging, test measurements, summaries, and structural performance reports.
 
