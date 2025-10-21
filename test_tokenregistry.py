# test_tokenregistry.py
"""
Tests for TokenRegistry module.
"""

import unittest
from tokenregistry import TokenRegistry

class TestTokenRegistry(unittest.TestCase):
    """Test cases for TokenRegistry class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenRegistry()
        self.assertIsInstance(instance, TokenRegistry)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenRegistry()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
