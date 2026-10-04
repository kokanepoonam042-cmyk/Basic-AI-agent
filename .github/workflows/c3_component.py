# SLE-3 - C3 Component Level
# Focus: Experiment Runner / Performance Analysis

CONTAINER_NAME = "Experiment Runner"


class Component:
    """Represent a component inside the Experiment Runner."""

    def __init__(self, name, responsibility):
        self.name = name
        self.responsibility = responsibility

    def display(self):
        print(f"{self.name}")
        print(f"  Responsibility: {self.responsibility}")


def define_components():

    components = [

        Component(
            "Algorithm Execution",
            "Executes BFS or DFS for the selected experiment."
        ),

        Component(
            "Performance Measurement",
            "Measures execution time using perf_counter()."
        ),

        Component(
            "Node Counting",
            "Records the number of nodes expanded."
        ),

        Component(
            "Result Collection",
            "Stores BFS and DFS times and node counts."
        ),

        Component(
            "Average Calculation",
            "Calculates average time and nodes across runs."
        ),

        Component(
            "Case Result",
            "Stores the final result for each test case."
        )
    ]

    return components


def component_overview():

    return {
        "container": CONTAINER_NAME,
        "components": define_components()
    }


if __name__ == "__main__":

    overview = component_overview()

    print("=" * 60)
    print("C3 - COMPONENT LEVEL")
    print("=" * 60)

    print("\nMAIN CONTAINER:")
    print(overview["container"])

    print("\nCOMPONENTS:\n")

    for component in overview["components"]:
        component.display()
        print()