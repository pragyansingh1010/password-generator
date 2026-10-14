## Password generator quality checks

- Ensure the requested length is validated against supported limits.
- Respect the user's selected character groups without silently adding excluded groups.
- Avoid returning an empty string when at least one valid character group is selected.
- Use a cryptographically secure random source when the runtime supports it.
- Make copy feedback explicit and avoid logging generated passwords.