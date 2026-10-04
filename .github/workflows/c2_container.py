SYSTEM_NAME = "BFS vs DFS Empirical Performance Analysis System"


class Container:
    """Represent a major container of the system."""

    def __init__(self, name, responsibility):
        self.name = name
        self.responsibility = responsibility

    def display(self):
        print(f"{self.name}")
        print(f"  Responsibility: {self.responsibility}")


def define_containers():

    containers = [

        Container(
            "Graph Creation",
            "Creates the 1200-node graph used for experiments."
        ),

        Container(
            "BFS Search",
            "Performs Breadth First Search using a FIFO queue."
        ),

        Container(
            "DFS Search",
            "Performs Depth First Search using a LIFO stack."
        ),

        Container(
            "Performance Measurement",
            "Measures execution time and counts expanded nodes."
        ),

        Container(
            "Experiment Runner",
            "Runs Best, Average and Worst case experiments."
        ),

        Container(
            "Result Summary",
            "Calculates averages and displays the final comparison."
        )
    ]

    return containers


def container_overview():

    return {
        "system": SYSTEM_NAME,
        "containers": define_containers()
    }


if __name__ == "__main__":

    overview = container_overview()

    print("=" * 60)
    print("C2 - CONTAINER LEVEL")
    print("=" * 60)

    print("\nSYSTEM:")
    print(overview["system"])

    print("\nCONTAINERS:\n")

    for container in overview["containers"]:
        container.display()
        print()
        from graphviz import Digraph
import os

dot = Digraph("C2_Container", format="png")
dot.attr(rankdir="TB")

dot.node("GC", "Graph Creation")
dot.node("BFS", "BFS Search")
dot.node("DFS", "DFS Search")
dot.node("PM", "Performance Measurement")
dot.node("ER", "Experiment Runner")
dot.node("RS", "Result Summary")

dot.edge("GC", "BFS")
dot.edge("GC", "DFS")
dot.edge("BFS", "PM")
dot.edge("DFS", "PM")
dot.edge("PM", "ER")
dot.edge("ER", "RS")

output_dir = os.path.join(os.path.dirname(__file__), "..", "Diagrams")
os.makedirs(output_dir, exist_ok=True)

dot.render(
    os.path.join(output_dir, "C2_container_diagram"),
    cleanup=True
)

print("C2 diagram generated successfully!")