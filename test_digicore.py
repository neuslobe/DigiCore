# test_digicore.py
"""
Tests for DigiCore module.
"""

import unittest
from digicore import DigiCore

class TestDigiCore(unittest.TestCase):
    """Test cases for DigiCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigiCore()
        self.assertIsInstance(instance, DigiCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigiCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
