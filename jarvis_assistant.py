"""
Jarvis AI Assistant - Main Module
A smooth functioning AI assistant with orb visualization
"""

import os
from datetime import datetime
from typing import Optional


class JarvisAssistant:
    """Main Jarvis AI Assistant Class"""
    
    def __init__(self, name: str = "Jarvis"):
        self.name = name
        self.initialized = False
        self.conversation_history = []
        self.response_count = 0
        
    def initialize(self) -> bool:
        """Initialize the Jarvis assistant"""
        try:
            self.initialized = True
            print(f"✓ {self.name} Assistant initialized successfully")
            return True
        except Exception as e:
            print(f"✗ Error initializing {self.name}: {e}")
            return False
    
    def process_input(self, user_input: str) -> str:
        """Process user input and generate response"""
        if not self.initialized:
            return "Assistant not initialized. Please call initialize() first."
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Store conversation
        self.conversation_history.append({
            "timestamp": timestamp,
            "input": user_input,
            "type": "user"
        })
        
        # Generate response based on input
        response = self._generate_response(user_input)
        
        # Store response
        self.conversation_history.append({
            "timestamp": timestamp,
            "response": response,
            "type": "assistant"
        })
        
        self.response_count += 1
        return response
    
    def _generate_response(self, user_input: str) -> str:
        """Generate appropriate response"""
        user_input_lower = user_input.lower().strip()
        
        # Greeting responses
        if any(word in user_input_lower for word in ["hello", "hi", "hey", "greetings"]):
            return f"Hello! I'm {self.name}. How can I assist you today?"
        
        # Help responses
        elif any(word in user_input_lower for word in ["help", "what can you do", "capabilities"]):
            return f"""I'm {self.name}, your AI assistant. I can help with:
- Answering questions
- Processing commands
- Managing tasks
- Providing information
- And much more! What would you like to know?"""
        
        # Status check
        elif any(word in user_input_lower for word in ["status", "how are you"]):
            return f"I'm running smoothly! All systems operational. Response count: {self.response_count}"
        
        # Time query
        elif "time" in user_input_lower:
            return f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # Default response
        else:
            return f"I received your message: '{user_input}'. How can I help you further?"
    
    def get_conversation_history(self) -> list:
        """Retrieve conversation history"""
        return self.conversation_history
    
    def clear_history(self) -> None:
        """Clear conversation history"""
        self.conversation_history = []
        self.response_count = 0
        print("Conversation history cleared.")
    
    def shutdown(self) -> None:
        """Shutdown the assistant gracefully"""
        self.initialized = False
        print(f"{self.name} Assistant shutdown successfully")


def main():
    """Main execution function"""
    print("=" * 50)
    print("JARVIS AI ASSISTANT - INITIALIZATION")
    print("=" * 50)
    
    # Initialize assistant
    jarvis = JarvisAssistant(name="Jarvis")
    jarvis.initialize()
    
    print("\nStarting interactive mode... (type 'exit' to quit)\n")
    
    # Interactive loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'exit':
                print("\nShutting down...")
                jarvis.shutdown()
                break
            
            if not user_input:
                continue
            
            response = jarvis.process_input(user_input)
            print(f"\n{jarvis.name}: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Shutting down...")
            jarvis.shutdown()
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
