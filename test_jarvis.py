"""
Jarvis Unit Tests
Test suite for core functionality
"""

import unittest
from jarvis_assistant import JarvisAssistant
from orb_visualization import JarvisOrb, OrbState


class TestJarvisAssistant(unittest.TestCase):
    """Test cases for JarvisAssistant"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.assistant = JarvisAssistant("TestJarvis")
    
    def test_initialization(self):
        """Test assistant initialization"""
        result = self.assistant.initialize()
        self.assertTrue(result)
        self.assertTrue(self.assistant.initialized)
    
    def test_greeting_response(self):
        """Test greeting responses"""
        self.assistant.initialize()
        response = self.assistant.process_input("hello")
        self.assertIn("Hello", response)
    
    def test_help_response(self):
        """Test help command response"""
        self.assistant.initialize()
        response = self.assistant.process_input("help")
        self.assertIn("can help with", response)
    
    def test_status_response(self):
        """Test status check"""
        self.assistant.initialize()
        response = self.assistant.process_input("status")
        self.assertIn("running smoothly", response)
    
    def test_conversation_history(self):
        """Test conversation history tracking"""
        self.assistant.initialize()
        self.assistant.process_input("hello")
        history = self.assistant.get_conversation_history()
        self.assertEqual(len(history), 2)  # User input + assistant response
    
    def test_clear_history(self):
        """Test clearing conversation history"""
        self.assistant.initialize()
        self.assistant.process_input("hello")
        self.assistant.clear_history()
        history = self.assistant.get_conversation_history()
        self.assertEqual(len(history), 0)
    
    def test_shutdown(self):
        """Test graceful shutdown"""
        self.assistant.initialize()
        self.assistant.shutdown()
        self.assertFalse(self.assistant.initialized)


class TestJarvisOrb(unittest.TestCase):
    """Test cases for JarvisOrb"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.orb = JarvisOrb()
    
    def test_orb_initialization(self):
        """Test orb initialization"""
        self.assertEqual(self.orb.state, OrbState.IDLE)
        self.assertFalse(self.orb.is_animating)
    
    def test_orb_idle_frame(self):
        """Test idle frame generation"""
        frame = self.orb._get_idle_frame(0)
        self.assertIsNotNone(frame)
        self.assertIn("◯", frame)
    
    def test_orb_processing_frame(self):
        """Test processing frame generation"""
        frame = self.orb._get_processing_frame(0)
        self.assertIsNotNone(frame)
        self.assertTrue(any(char in frame for char in ["●", "◯"]))
    
    def test_orb_reset(self):
        """Test orb reset"""
        self.orb.state = OrbState.PROCESSING
        self.orb.reset()
        self.assertEqual(self.orb.state, OrbState.IDLE)
        self.assertFalse(self.orb.is_animating)


class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def test_assistant_orb_integration(self):
        """Test assistant and orb working together"""
        assistant = JarvisAssistant()
        orb = JarvisOrb()
        
        # Initialize
        assistant.initialize()
        
        # Simulate interaction
        response = assistant.process_input("hello")
        
        # Verify
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)


if __name__ == "__main__":
    unittest.main()
