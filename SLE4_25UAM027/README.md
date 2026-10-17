# SLE-4: Final Viva & Architecture Decision Record (ADR)

## Course Information
- **Course Code:** 02AML204
- **Course Name:** Introduction to Artificial Intelligence
- **Student Name:** Poonam Arjun Kokane
- **PRN:** 25UAM027
- **Division:** A
- **Project Title:** BFS vs DFS Empirical Performance Analysis System
- **ADR Status:** Accepted
- **Decision Date:** 10 October 2026

---

## 1. Introduction

SLE-4 focuses on the final viva and Architecture Decision Record (ADR) for the BFS vs DFS Empirical Performance Analysis System.

The project compares Breadth-First Search (BFS) and Depth-First Search (DFS) using a graph containing 1,200 nodes. The algorithms are evaluated using execution time and the number of nodes expanded.

## 2. Objectives

- To summarize the work completed in SLE-1, SLE-2, and SLE-3.
- To compare BFS and DFS performance.
- To document the final architecture decision.
- To understand the advantages and limitations of both algorithms.
- To prepare for the final project viva.

## 3. Architecture Decision Record (ADR)

### Title
**ADR 1: Selection of BFS and DFS for Comparative Graph Search Analysis**

### Status
Accepted

### Context

The project aims to study the practical performance of two graph search algorithms, BFS and DFS, on the same connected graph containing 1,200 nodes.

The performance is measured using execution time and the number of nodes expanded for different target positions.

### Alternatives Considered

1. **BFS only:** Explores nodes level by level.
2. **DFS only:** Explores one path deeply before backtracking.
3. **A* Search:** Uses path cost and a heuristic to guide the search.

### Decision

Both BFS and DFS were selected for implementation and comparison. The same graph and test conditions are used to observe their practical performance.

### Consequences

**Advantages**
- Enables comparison of two graph search algorithms.
- Helps understand execution time and node expansion.
- Supports the analysis of best-case, average-case, and worst-case scenarios.
- Makes the system architecture easier to explain.

**Limitations**
- BFS may require more memory for its queue.
- DFS does not guarantee the shortest path.
- Results depend on graph structure, traversal order, and target position.

## 4. Empirical Performance Analysis

The following measurements are from the project's SLE-2 report. Execution times may vary between runs and computers.

| Case | Target | BFS Time (ms) | DFS Time (ms) | BFS Nodes | DFS Nodes |
|---|---|---:|---:|---:|---:|
| Best | 1 | 0.00261 | 0.214