# Password Generator Safety Notes

- Use a cryptographically secure random source when available.
- Avoid using `Math.random()` for security-sensitive password generation.
- Make selected character sets and length visible to the user.
- Ensure the chosen length is within supported bounds.
- Do not save generated passwords to local storage by default.
- Do not log passwords to the console.