"""
Advanced Examples for Jarvis-bubble
Demonstrates advanced usage patterns and customization
"""

from jarvis_assistant import JarvisAssistant
from orb_visualization import JarvisOrb, OrbState
from config_manager import ConfigManager
from logger import logger
import time


class AdvancedJarvisExample:
    """Advanced usage examples"""
    
    @staticmethod
    def example_1_custom_assistant():
        """Example 1: Create custom assistant with custom name"""
        print("\n" + "=" * 60)
        print("EXAMPLE 1: Custom Assistant Configuration")
        print("=" * 60 + "\n")
        
        # Create custom assistant
        assistant = JarvisAssistant(name="FRIDAY")
        assistant.initialize()
        
        # Interact
        responses = [
            "hello",
            "what can you do",
            "status",
            "exit"
        ]
        
        for user_input in responses:
            if user_input.lower() == 'exit':
                break
            response = assistant.process_input(user_input)
            print(f"You: {user_input}")
            print(f"FRIDAY: {response}\n")
        
        assistant.shutdown()
    
    @staticmethod
    def example_2_orb_states():
        """Example 2: Demonstrate all orb states"""
        print("\n" + "=" * 60)
        print("EXAMPLE 2: Orb States Demonstration")
        print("=" * 60 + "\n")
        
        orb = JarvisOrb()
        
        states = [
            (OrbState.IDLE, "Idle - Waiting"),
            (OrbState.LISTENING, "Listening - Processing input"),
            (OrbState.PROCESSING, "Processing - Analyzing"),
            (OrbState.RESPONDING, "Responding - Generating output"),
        ]
        
        for state, description in states:
            print(f"\n→ {description}")
            orb.animate(state, duration=1.5)
    
    @staticmethod
    def example_3_conversation_tracking():
        """Example 3: Track and analyze conversations"""
        print("\n" + "=" * 60)
        print("EXAMPLE 3: Conversation Tracking")
        print("=" * 60 + "\n")
        
        assistant = JarvisAssistant()
        assistant.initialize()
        
        # Simulate conversation
        inputs = ["hello", "help", "status", "what time is it"]
        
        for user_input in inputs:
            assistant.process_input(user_input)
        
        # Analyze
        history = assistant.get_conversation_history()
        print(f"\nTotal interactions: {len(history)}")
        print(f"Response count: {assistant.response_count}\n")
        
        print("Conversation Log:")
        for i, item in enumerate(history, 1):
            if item["type"] == "user":
                print(f"  {i}. User: {item['input']}")
            else:
                print(f"  {i}. Jarvis: {item['response']}")
        
        assistant.shutdown()
    
    @staticmethod
    def example_4_configuration():
        """Example 4: Load and use configuration"""
        print("\n" + "=" * 60)
        print("EXAMPLE 4: Configuration Management")
        print("=" * 60 + "\n")
        
        config = ConfigManager()
        
        # Get configurations
        assistant_config = config.get_assistant_config()
        orb_config = config.get_orb_config()
        behavior_config = config.get_behavior_config()
        
        print("Assistant Configuration:")
        for key, value in assistant_config.items():
            print(f"  {key}: {value}")
        
        print("\nOrb Configuration:")
        for key, value in orb_config.items():
            print(f"  {key}: {value}")
        
        print("\nBehavior Configuration:")
        for key, value in behavior_config.items():
            print(f"  {key}: {value}")
    
    @staticmethod
    def example_5_logging():
        """Example 5: Logging interactions"""
        print("\n" + "=" * 60)
        print("EXAMPLE 5: Logging System")
        print("=" * 60 + "\n")
        
        assistant = JarvisAssistant()
        assistant.initialize()
        
        # Log interactions
        test_inputs = ["hello", "help"]
        
        for user_input in test_inputs:
            response = assistant.process_input(user_input)
            logger.log_interaction(user_input, response)
        
        logger.info("Example interaction logging complete")
        print("✓ Interactions logged to logs/ directory")
        
        assistant.shutdown()
    
    @staticmethod
    def example_6_custom_responses():
        """Example 6: Extend with custom responses"""
        print("\n" + "=" * 60)
        print("EXAMPLE 6: Custom Response Handling")
        print("=" * 60 + "\n")
        
        class CustomAssistant(JarvisAssistant):
            """Extended assistant with custom responses"""
            
            def _generate_response(self, user_input: str) -> str:
                user_input_lower = user_input.lower().strip()
                
                # Custom responses
                if "joke" in user_input_lower:
                    return "Why did the AI go to school? To improve its learning model! 😄"
                
                elif "calculate" in user_input_lower:
                    return "I can help with calculations. Please provide the numbers and operation."
                
                else:
                    # Fall back to parent implementation
                    return super()._generate_response(user_input)
        
        assistant = CustomAssistant(name="SmartJarvis")
        assistant.initialize()
        
        # Test custom responses
        test_inputs = ["tell me a joke", "calculate something", "hello"]
        
        for user_input in test_inputs:
            response = assistant.process_input(user_input)
            print(f"You: {user_input}")
            print(f"SmartJarvis: {response}\n")
        
        assistant.shutdown()
    
    @staticmethod
    def example_7_performance():
        """Example 7: Performance testing"""
        print("\n" + "=" * 60)
        print("EXAMPLE 7: Performance Testing")
        print("=" * 60 + "\n")
        
        assistant = JarvisAssistant()
        assistant.initialize()
        
        # Test response time
        test_inputs = [
            "hello",
            "help",
            "status",
            "what time is it",
            "how are you"
        ]
        
        print("Response Time Analysis:")
        start_time = time.time()
        
        for user_input in test_inputs:
            response = assistant.process_input(user_input)
        
        total_time = time.time() - start_time
        avg_time = total_time / len(test_inputs)
        
        print(f"  Total time: {total_time:.4f}s")
        print(f"  Average response time: {avg_time:.4f}s")
        print(f"  Requests processed: {assistant.response_count}")
        
        assistant.shutdown()


def run_all_examples():
    """Run all examples"""
    examples = [
        ("Custom Assistant", AdvancedJarvisExample.example_1_custom_assistant),
        ("Orb States", AdvancedJarvisExample.example_2_orb_states),
        ("Conversation Tracking", AdvancedJarvisExample.example_3_conversation_tracking),
        ("Configuration", AdvancedJarvisExample.example_4_configuration),
        ("Logging", AdvancedJarvisExample.example_5_logging),
        ("Custom Responses", AdvancedJarvisExample.example_6_custom_responses),
        ("Performance Testing", AdvancedJarvisExample.example_7_performance),
    ]
    
    print("\n" + "=" * 60)
    print("JARVIS-BUBBLE ADVANCED EXAMPLES")
    print("=" * 60)
    
    for i, (name, example_func) in enumerate(examples, 1):
        try:
            example_func()
        except Exception as e:
            print(f"\n✗ Error in {name}: {e}")
        
        if i < len(examples):
            print("\n" + "-" * 60)
            input("Press Enter to continue to next example...")
    
    print("\n" + "=" * 60)
    print("All examples completed! ✓")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_examples()
