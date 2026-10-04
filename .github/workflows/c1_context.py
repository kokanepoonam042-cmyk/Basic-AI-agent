import os

# ---------------------------------------------------------
# 1. Automatically find Graphviz
# ---------------------------------------------------------

graphviz_bin = r"C:\Program Files\Graphviz\bin"

if os.path.exists(os.path.join(graphviz_bin, "dot.exe")):
    os.environ["PATH"] += os.pathsep + graphviz_bin


# ---------------------------------------------------------
# 2. Import diagram libraries
# ---------------------------------------------------------

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank


# ---------------------------------------------------------
# 3. Output path
# ---------------------------------------------------------

output_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Diagrams")
)

os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(
    output_dir,
    "C1_context_diagram"
)


# ---------------------------------------------------------
# 4. Diagram appearance
# ---------------------------------------------------------

graph_attr = {
    "bgcolor": "white",
    "fontsize": "20",
    "fontcolor": "black",
    "pad": "0.5",
    "nodesep": "1.2",
    "ranksep": "1.5"
}


# ---------------------------------------------------------
# 5. Generate C1 Context Diagram
# ---------------------------------------------------------

with Diagram(
    "C1 - CONTEXT LEVEL\nBFS vs DFS Empirical Performance Analysis System",
    filename=output_file,
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr
):

    # External Actor
    user = Blank("Student / User")


    # System Boundary
    with Cluster(
        "System Boundary",
        graph_attr={
            "bgcolor": "lightblue",
            "fontcolor": "black",
            "fontsize": "18"
        }
    ):

        system = Blank(
            "BFS vs DFS System\n\n"
            "Responsibilities:\n"
            "• Create Graph (1200 nodes)\n"
            "• Execute BFS & DFS\n"
            "• Measure Performance\n"
            "• Compare Results"
        )


    # Input flow
    user >> Edge(
        label="Graph\nStart Node\nTarget Node\nBFS / DFS",
        color="black",
        fontcolor="black"
    ) >> system


    # Output flow
    system >> Edge(
        label="Search Result\nNodes Expanded\nPerformance Results",
        color="black",
        fontcolor="black"
    ) >> user


# ---------------------------------------------------------
# 6. Automatically open generated PNG
# ---------------------------------------------------------

if __name__ == "__main__":

    png_file = output_file + ".png"

    print("=" * 60)
    print("C1 CONTEXT DIAGRAM GENERATED")
    print("=" * 60)
    print()
    print("PNG FILE:")
    print(png_file)
    print()

    if os.path.exists(png_file):

        print("SUCCESS: C1_context_diagram.png created.")

        # Automatically open the generated PNG in Windows
        os.startfile(png_file)

    else:

        print("ERROR: PNG file was not generated.")