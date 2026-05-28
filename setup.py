"""
Jarvis Setup Script
Quick installation and setup for the project
"""

import os
import sys
import subprocess


def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def check_python_version():
    """Check Python version compatibility"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("✗ Python 3.7+ is required")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    return True


def install_dependencies():
    """Install project dependencies"""
    try:
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed")
        return True
    except Exception as e:
        print(f"✗ Error installing dependencies: {e}")
        return False


def create_directories():
    """Create necessary directories"""
    directories = ["logs", "data", "cache"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Created {directory}/ directory")
        else:
            print(f"✓ {directory}/ directory exists")


def verify_files():
    """Verify essential files exist"""
    required_files = [
        "main.py",
        "jarvis_assistant.py",
        "orb_visualization.py",
        "config_manager.py",
        "logger.py",
        "config.ini",
        "requirements.txt",
    ]
    
    print("Checking required files...")
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} (missing)")
            all_exist = False
    
    return all_exist


def run_tests():
    """Run unit tests"""
    print("Running tests...")
    try:
        subprocess.check_call([sys.executable, "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py"])
        print("✓ All tests passed")
        return True
    except subprocess.CalledProcessError:
        print("✗ Some tests failed")
        return False


def main():
    """Main setup function"""
    print_header("JARVIS-BUBBLE SETUP")
    
    # Check Python version
    print("Checking Python version...")
    if not check_python_version():
        return False
    
    # Verify files
    print("\nVerifying files...")
    if not verify_files():
        print("\n⚠ Warning: Some files are missing")
    
    # Create directories
    print("\nCreating directories...")
    create_directories()
    
    # Install dependencies
    print("\nInstalling dependencies...")
    if not install_dependencies():
        return False
    
    # Run tests
    print("\nRunning tests...")
    if not run_tests():
        print("\n⚠ Warning: Some tests failed")
    
    # Success
    print_header("SETUP COMPLETE ✓")
    print("Next steps:")
    print("  1. Run the assistant: python main.py")
    print("  2. Check documentation: cat README.md")
    print("  3. View options: make help")
    print("\nHappy coding! 🤖\n")
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Setup failed: {e}")
        sys.exit(1)
