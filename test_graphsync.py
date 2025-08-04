# test_graphsync.py
"""
Tests for GraphSync module.
"""

import unittest
from graphsync import GraphSync

class TestGraphSync(unittest.TestCase):
    """Test cases for GraphSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GraphSync()
        self.assertIsInstance(instance, GraphSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GraphSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
