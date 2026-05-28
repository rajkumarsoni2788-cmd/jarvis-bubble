"""
Jarvis AI Assistant - Main Entry Point
Combines smooth assistant functionality with orb visualization
"""

from jarvis_assistant import JarvisAssistant
from orb_visualization import JarvisOrb, OrbState
import time


class JarvisSystem:
    """Complete Jarvis system with assistant and orb"""
    
    def __init__(self):
        self.assistant = JarvisAssistant(name="Jarvis")
        self.orb = JarvisOrb()
        self.running = False
    
    def startup(self) -> None:
        """Initialize the complete system"""
        print("\n" + "=" * 60)
        print("JARVIS AI ASSISTANT SYSTEM - STARTUP SEQUENCE")
        print("=" * 60 + "\n")
        
        # Initialize assistant
        print("► Initializing AI Assistant...")
        self.orb.animate(OrbState.PROCESSING, duration=1.5)
        self.assistant.initialize()
        
        # Show idle orb
        print("► System ready")
        self.orb.animate(OrbState.IDLE, duration=1.0)
        
        self.running = True
        print("\n✓ Jarvis System is ready!\n")
    
    def process_command(self, user_input: str) -> None:
        """Process user command with orb feedback"""
        if not user_input.strip():
            return
        
        # Listening state
        self.orb.animate(OrbState.LISTENING, duration=0.8)
        
        # Processing state
        self.orb.animate(OrbState.PROCESSING, duration=1.0)
        
        # Get response
        response = self.assistant.process_input(user_input)
        
        # Responding state with pulse
        self.orb.pulse(intensity=2)
        
        # Display response
        print(f"Jarvis: {response}\n")
    
    def shutdown(self) -> None:
        """Shutdown the system gracefully"""
        print("\n► Shutting down Jarvis System...")
        self.orb.animate(OrbState.IDLE, duration=1.0)
        self.assistant.shutdown()
        self.running = False
        print("✓ Jarvis System shutdown complete\n")
    
    def run_interactive(self) -> None:
        """Run interactive mode"""
        self.startup()
        
        print("Commands: 'help', 'history', 'clear', 'exit'\n")
        
        while self.running:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle special commands
                if user_input.lower() == 'exit':
                    self.shutdown()
                    break
                
                elif user_input.lower() == 'history':
                    history = self.assistant.get_conversation_history()
                    if history:
                        print("\n[Conversation History]")
                        for item in history:
                            if item["type"] == "user":
                                print(f"  You: {item['input']}")
                            else:
                                print(f"  Jarvis: {item['response']}")
                        print()
                    else:
                        print("No conversation history yet.\n")
                
                elif user_input.lower() == 'clear':
                    self.assistant.clear_history()
                
                else:
                    # Process regular input
                    self.process_command(user_input)
                
            except KeyboardInterrupt:
                print("\n")
                self.shutdown()
                break
            except Exception as e:
                print(f"✗ Error: {e}\n")
                self.orb.flash_error()


def main():
    """Main entry point"""
    system = JarvisSystem()
    system.run_interactive()


if __name__ == "__main__":
    main()
