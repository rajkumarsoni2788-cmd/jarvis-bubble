# Jarvis-bubble Development Guidelines

## Code Style

- **Language**: Python 3.7+
- **Style Guide**: PEP 8
- **Line Length**: 100 characters max
- **Type Hints**: Encouraged for public methods

## Project Structure

```
jarvis-bubble/
├── main.py                  # Entry point
├── jarvis_assistant.py      # Core AI logic
├── orb_visualization.py     # UI/Animation
├── config_manager.py        # Configuration handling
├── logger.py               # Logging system
├── test_jarvis.py          # Unit tests
├── config.ini              # Configuration file
├── requirements.txt        # Dependencies
├── Makefile               # Build commands
├── README.md              # Documentation
└── .github/workflows/     # CI/CD pipelines
```

## Development Workflow

1. **Create a branch**: `git checkout -b feature/your-feature`
2. **Make changes**: Edit files and test locally
3. **Run tests**: `make test` or `python -m unittest discover`
4. **Format code**: `make format` or use Black
5. **Commit**: `git commit -m "Description of changes"`
6. **Push**: `git push origin feature/your-feature`
7. **Create PR**: Open pull request on GitHub

## Testing

### Run All Tests
```bash
make test
```

### Run Specific Test
```bash
python -m unittest test_jarvis.TestJarvisAssistant.test_initialization
```

### Run with Verbose Output
```bash
make test-verbose
```

### Test Coverage
```bash
pip install coverage
coverage run -m unittest discover
coverage report
```

## Adding New Features

### Adding New Assistant Responses

Edit `jarvis_assistant.py` in `_generate_response()`:

```python
elif "your_keyword" in user_input_lower:
    return "Your response here"
```

### Adding New Orb States

1. Add state to `OrbState` enum in `orb_visualization.py`
2. Create `_get_[state_name]_frame()` method
3. Add case in `animate()` method
4. Add test case in `test_jarvis.py`

### Adding Configuration Options

1. Add section in `config.ini`
2. Add getter method in `ConfigManager` class
3. Update documentation in `DEVELOPMENT.md`

## Debugging

### Enable Debug Logging
```python
from logger import logger
logger.debug("Your debug message")
```

### Test Individual Modules
```bash
python jarvis_assistant.py      # Test assistant
python orb_visualization.py     # Test orb
python config_manager.py        # Test config
python logger.py               # Test logger
```

## Performance Considerations

- Keep animation frame updates under 100ms
- Limit conversation history to configurable size
- Use generators for large data sets
- Cache frequently accessed configs

## Common Issues & Solutions

### Issue: Orb animation not showing
**Solution**: Check Unicode support, ensure terminal supports UTF-8

### Issue: Config not loading
**Solution**: Verify `config.ini` exists in project root

### Issue: Tests failing on import
**Solution**: Ensure all files in same directory, check PYTHONPATH

## Release Checklist

- [ ] All tests passing
- [ ] Code formatted with Black
- [ ] Documentation updated
- [ ] Version bumped in `config.ini`
- [ ] CHANGELOG updated
- [ ] README reviewed
- [ ] No uncommitted changes
- [ ] Tag release on GitHub

## Contributing

1. Follow PEP 8 style guide
2. Add tests for new features
3. Update documentation
4. Keep commits atomic and descriptive
5. Reference issues in commit messages

## Resources

- [Python PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [Real Python Style Guide](https://realpython.com/)
- [Python Logging](https://docs.python.org/3/library/logging.html)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)

## Questions?

Open an issue on GitHub or check the README for more information.
