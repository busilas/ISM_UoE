import json
import matplotlib.pyplot as plt
from attack_tree import load_json, load_yaml, load_xml, AttackTreeNode

# Function to visualize the attack tree using matplotlib
def visualize_attack_tree(node, graph=None, parent=None, depth=0, pos=None, x=0.5, y=1.0, level_width=0.2):
    if graph is None:
        fig, graph = plt.subplots()
    if pos is None:
        pos = {}
    pos[node.name] = (x, y)  # Store node position
    if parent:
        # Draw line from parent to current node
        graph.plot([pos[parent][0], pos[node.name][0]], [pos[parent][1], pos[node.name][1]], 'k-')
    # Draw the node name
    graph.text(x, y, node.name, ha='center', va='center', bbox=dict(facecolor='w', edgecolor='k'))
    y -= 0.1
    num_children = len(node.children)
    if num_children > 1:
        level_width = level_width / num_children  # Adjust width based on number of children
    for i, child in enumerate(node.children):
        visualize_attack_tree(child, graph, node.name, depth + 1, pos, x - level_width/2 + i*level_width, y, level_width)
    return graph

# Function to export the visualized attack tree to a file
def export_attack_tree(graph, filename):
    graph.figure.savefig(filename)

# Main application function
def main():
    attack_tree = None
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Load Attack Tree from File")
        print("2. Visualize Attack Tree")
        print("3. Add Leaf Node Values")
        print("4. Aggregate Values and Calculate Total Threat Value")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            file_path = input("Enter file path: ")
            file_type = file_path.split('.')[-1]
            if file_type == 'json':
                attack_tree = load_json(file_path)
            elif file_type == 'yaml' or file_type == 'yml':
                attack_tree = load_yaml(file_path)
            elif file_type == 'xml':
                attack_tree = load_xml(file_path)
            else:
                print("Unsupported file type.")

        elif choice == '2':
            if attack_tree:
                graph = visualize_attack_tree(attack_tree)
                plt.show()
            else:
                print("No attack tree loaded.")

        elif choice == '3':
            if attack_tree:
                values = input("Enter node values as JSON: ")
                values = json.loads(values)
                attack_tree.add_values_to_node(values)
            else:
                print("No attack tree loaded.")

        elif choice == '4':
            if attack_tree:
                total_value = attack_tree.calculate_total_value()
                print(f"Total Threat Value: {total_value}")
                graph = visualize_attack_tree(attack_tree)
                file_name = input("Enter file name to save the tree (e.g., tree.png): ")
                export_attack_tree(graph, file_name)
            else:
                print("No attack tree loaded.")

        elif choice == '5':
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
