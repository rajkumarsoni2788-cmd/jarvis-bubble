# Contributing to Jarvis-bubble

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the Jarvis-bubble project.

## Code of Conduct

Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

1. Check existing issues to avoid duplicates
2. Create a new issue with clear title and description
3. Include steps to reproduce
4. Provide Python version and OS information
5. Add relevant error messages or logs

### Suggesting Enhancements

1. Use the issue tracker
2. Clearly describe the enhancement
3. Explain the use case and benefits
4. Provide examples if applicable

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes following PEP 8
4. Add or update tests as needed
5. Update documentation
6. Commit with clear messages
7. Push to your fork
8. Create a pull request with detailed description

## Development Setup

```bash
# Clone the repository
git clone https://github.com/rajkumarsoni2788-cmd/Jarvis-bubble.git
cd Jarvis-bubble

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
make setup-dev

# Run tests
make test
```

## Coding Standards

### Style Guide
- Follow PEP 8
- Line length: 100 characters max
- Use type hints for public methods
- Write docstrings for classes and methods

### Example
```python
def process_input(self, user_input: str) -> str:
    """
    Process user input and generate response.
    
    Args:
        user_input: The user's input string
    
    Returns:
        The assistant's response string
    """
    pass
```

### Testing Requirements
- Write tests for new features
- Maintain or improve test coverage
- Run tests before submitting PR
- Use meaningful test names

```python
def test_greeting_response(self):
    """Test that greetings are properly recognized"""
    self.assistant.initialize()
    response = self.assistant.process_input("hello")
    self.assertIn("Hello", response)
```

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
[Feature/Fix/Docs] Brief description

Detailed explanation of changes made and why.
- Bullet point for each major change
- Reference issues: Closes #123
```

Examples:
```
Fix: Correct orb animation timing issue

- Reduced animation frame delay from 200ms to 100ms
- Fixed Unicode character rendering on Windows
- Closes #45

Feature: Add conversation history export

- Users can now export chat history as JSON
- Added export_history() method to JarvisAssistant
- Includes tests for export functionality
```

## Documentation

### Update These Files
- **README.md**: User-facing documentation
- **DEVELOPMENT.md**: Developer documentation
- **CHANGELOG.md**: Version history
- **Code comments**: Explain complex logic

### Documentation Standards
- Use clear, simple language
- Include examples where applicable
- Keep documentation up-to-date with code
- Use Markdown formatting

## Testing

```bash
# Run all tests
make test

# Run specific test
python -m unittest test_jarvis.TestJarvisAssistant.test_initialization

# Run with coverage
pip install coverage
coverage run -m unittest discover
coverage report
```

## Project Structure

```
jarvis-bubble/
├── main.py                    # Entry point
├── jarvis_assistant.py        # Core logic
├── orb_visualization.py       # UI/Animation
├── config_manager.py          # Configuration
├── logger.py                  # Logging
├── test_jarvis.py             # Tests
├── config.ini                 # Settings
├── requirements.txt           # Dependencies
├── Makefile                   # Build commands
├── DEVELOPMENT.md             # Dev guide
├── CONTRIBUTING.md            # This file
├── CHANGELOG.md               # Version history
└── README.md                  # User guide
```

## Review Process

1. Maintainers review your PR
2. Address any comments or suggestions
3. Make requested changes
4. Ensure tests pass
5. PR is merged once approved

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- CHANGELOG.md
- README.md (if significant contribution)

## Questions?

- Open an issue for bugs
- Start a discussion for questions
- Check existing documentation first

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to Jarvis-bubble! 🤖✨
