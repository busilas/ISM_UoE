import unittest
from unittest.mock import patch, mock_open
from attack_tree import AttackTreeNode, load_json, load_yaml, load_xml
import main

class TestAttackTreeNode(unittest.TestCase):

    def setUp(self):
        self.root = AttackTreeNode(name="Root")
        self.child1 = AttackTreeNode(name="Child1")
        self.child2 = AttackTreeNode(name="Child2", value=10)
        self.root.add_child(self.child1)
        self.root.add_child(self.child2)
        self.child1_1 = AttackTreeNode(name="Child1_1", value=5)
        self.child1.add_child(self.child1_1)

    def test_add_child(self):
        self.assertEqual(len(self.root.children), 2)
        self.assertIn(self.child1, self.root.children)
        self.assertIn(self.child2, self.root.children)

    def test_calculate_total_value(self):
        total_value = self.root.calculate_total_value()
        self.assertEqual(total_value, 15)

    def test_add_values_to_node(self):
        self.root.add_values_to_node({"Child1": 7, "Child2": 3, "Child1_1": 8})
        self.assertEqual(self.child1.value, 7)
        self.assertEqual(self.child2.value, 3)
        self.assertEqual(self.child1_1.value, 8)

class TestMainFunctions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"name": "Root", "children": [{"name": "Child1"}, {"name": "Child2", "value": 10}]}')
    def test_load_json(self, mock_file):
        tree = load_json('test.json')
        self.assertEqual(tree.name, "Root")
        self.assertEqual(len(tree.children), 2)
        self.assertEqual(tree.children[1].value, 10)

    @patch('builtins.open', new_callable=mock_open, read_data='name: Root\nchildren:\n  - name: Child1\n  - name: Child2\n    value: 10\n')
    def test_load_yaml(self, mock_file):
        tree = load_yaml('test.yaml')
        self.assertEqual(tree.name, "Root")
        self.assertEqual(len(tree.children), 2)
        self.assertEqual(tree.children[1].value, 10)

    @patch('builtins.open', new_callable=mock_open, read_data='<node name="Root"><node name="Child1"/><node name="Child2" value="10"/></node>')
    def test_load_xml(self, mock_file):
        tree = load_xml('test.xml')
        self.assertEqual(tree.name, "Root")
        self.assertEqual(len(tree.children), 2)
        self.assertEqual(tree.children[1].value, 10)

    @patch('builtins.input', side_effect=['5'])
    def test_main_exit(self, mock_input):
        with patch('builtins.print') as mocked_print:
            main.main()
            mocked_print.assert_any_call("\nMenu:")
            mocked_print.assert_any_call("1. Load Attack Tree from File")
            mocked_print.assert_any_call("2. Visualize Attack Tree")
            mocked_print.assert_any_call("3. Add Leaf Node Values")
            mocked_print.assert_any_call("4. Aggregate Values and Calculate Total Threat Value")
            mocked_print.assert_any_call("5. Exit")

if __name__ == '__main__':
    unittest.main()
