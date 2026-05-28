"""
Jarvis Logging Module
Handles logging for the Jarvis system
"""

import logging
import os
from datetime import datetime
from typing import Optional


class JarvisLogger:
    """Custom logger for Jarvis system"""
    
    def __init__(self, name: str = "Jarvis", log_dir: str = "logs"):
        self.name = name
        self.log_dir = log_dir
        self.logger = None
        self.setup_logger()
    
    def setup_logger(self) -> None:
        """Setup logger with file and console handlers"""
        # Create logs directory if it doesn't exist
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        
        # Create logger
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        
        # Create formatters
        detailed_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        simple_formatter = logging.Formatter(
            '%(levelname)s: %(message)s'
        )
        
        # File handler (detailed logs)
        log_file = os.path.join(self.log_dir, f"jarvis_{datetime.now().strftime('%Y%m%d')}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        
        # Console handler (simple logs)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(simple_formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.info(f"{self.name} Logger initialized")
    
    def info(self, message: str) -> None:
        """Log info message"""
        if self.logger:
            self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log warning message"""
        if self.logger:
            self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Log error message"""
        if self.logger:
            self.logger.error(message)
    
    def debug(self, message: str) -> None:
        """Log debug message"""
        if self.logger:
            self.logger.debug(message)
    
    def log_interaction(self, user_input: str, response: str) -> None:
        """Log user interaction"""
        if self.logger:
            self.logger.info(f"USER: {user_input}")
            self.logger.info(f"RESPONSE: {response}")


# Default logger instance
logger = JarvisLogger()


if __name__ == "__main__":
    # Test logging
    test_logger = JarvisLogger()
    test_logger.info("Test info message")
    test_logger.warning("Test warning message")
    test_logger.error("Test error message")
    test_logger.debug("Test debug message")
    test_logger.log_interaction("Hello Jarvis", "Hello! How can I assist you?")
