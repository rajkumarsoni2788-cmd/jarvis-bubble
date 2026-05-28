"""
Jarvis Configuration Manager
Handles loading and managing configuration settings
"""

import configparser
import os
from typing import Any, Optional


class ConfigManager:
    """Manages configuration for Jarvis system"""
    
    def __init__(self, config_file: str = "config.ini"):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.load_config()
    
    def load_config(self) -> bool:
        """Load configuration from file"""
        try:
            if os.path.exists(self.config_file):
                self.config.read(self.config_file)
                return True
            else:
                print(f"Warning: Config file '{self.config_file}' not found. Using defaults.")
                return False
        except Exception as e:
            print(f"Error loading config: {e}")
            return False
    
    def get(self, section: str, key: str, fallback: Any = None) -> Any:
        """Get configuration value"""
        try:
            if self.config.has_option(section, key):
                value = self.config.get(section, key)
                # Try to convert to appropriate type
                if value.lower() in ('true', 'false'):
                    return value.lower() == 'true'
                try:
                    return int(value)
                except ValueError:
                    try:
                        return float(value)
                    except ValueError:
                        return value
            return fallback
        except Exception as e:
            print(f"Error getting config value {section}.{key}: {e}")
            return fallback
    
    def get_assistant_config(self) -> dict:
        """Get assistant configuration"""
        return {
            'name': self.get('assistant', 'name', 'Jarvis'),
            'version': self.get('assistant', 'version', '1.0.0'),
            'description': self.get('assistant', 'description', 'AI Assistant'),
        }
    
    def get_orb_config(self) -> dict:
        """Get orb configuration"""
        return {
            'size': self.get('orb', 'size', 5),
            'animation_speed': self.get('orb', 'animation_speed', 0.1),
            'pulse_intensity': self.get('orb', 'pulse_intensity', 3),
        }
    
    def get_behavior_config(self) -> dict:
        """Get behavior configuration"""
        return {
            'max_history_size': self.get('behavior', 'max_history_size', 100),
            'response_timeout': self.get('behavior', 'response_timeout', 30),
            'enable_logging': self.get('behavior', 'enable_logging', True),
        }
    
    def print_config(self) -> None:
        """Print all configuration"""
        print("\n" + "=" * 50)
        print("JARVIS CONFIGURATION")
        print("=" * 50)
        
        for section in self.config.sections():
            print(f"\n[{section}]")
            for key, value in self.config.items(section):
                print(f"  {key} = {value}")
        
        print("\n" + "=" * 50 + "\n")


# Default configuration instance
config = ConfigManager()


if __name__ == "__main__":
    # Test configuration loading
    cfg = ConfigManager()
    cfg.print_config()
    
    print("Assistant Config:", cfg.get_assistant_config())
    print("Orb Config:", cfg.get_orb_config())
    print("Behavior Config:", cfg.get_behavior_config())
