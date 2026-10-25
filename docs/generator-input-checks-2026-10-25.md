## Generator input checks

- Validate requested length before generating a password.
- Require at least one enabled character group.
- Ensure generated output length matches the selected length.
- Use secure randomness when supported by the runtime.
- Never print or store generated passwords in diagnostic logs.