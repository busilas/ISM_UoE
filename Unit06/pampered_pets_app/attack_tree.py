import json
import yaml
import xml.etree.ElementTree as ET

# AttackTreeNode class represents a node in the attack tree
class AttackTreeNode:
    def __init__(self, name, value=0):
        self.name = name  # Node name
        self.value = value  # Initial value for the node
        self.children = []  # List to hold child nodes

    # Method to add a child node to the current node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Method to calculate the total value of the tree from this node
    def calculate_total_value(self):
        total_value = self.value  # Start with the node's own value
        for child in self.children:
            total_value += child.calculate_total_value()  # Add values of child nodes recursively
        return total_value

    # Method to add values to nodes based on a dictionary of values
    def add_values_to_node(self, values):
        if self.name in values:
            self.value = values[self.name]
        for child in self.children:
            child.add_values_to_node(values)

# Function to build an attack tree from a dictionary (parsed JSON/YAML)
def build_tree(data):
    node = AttackTreeNode(name=data['name'], value=data.get('value', 0))
    for child_data in data.get('children', []):
        child_node = build_tree(child_data)
        node.add_child(child_node)
    return node

# Function to build an attack tree from an XML element
def build_tree_xml(element):
    node = AttackTreeNode(name=element.attrib['name'], value=int(element.attrib.get('value', 0)))
    for child in element.findall('node'):
        child_node = build_tree_xml(child)
        node.add_child(child_node)
    return node

# Function to load an attack tree from a JSON file
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return build_tree(data)

# Function to load an attack tree from a YAML file
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return build_tree(data)

# Function to load an attack tree from an XML file
def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return build_tree_xml(root)
