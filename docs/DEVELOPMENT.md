# Development Notes

Password generation should use the browser's cryptographic random source where available. Keep generated values out of logs and avoid storing passwords unless the feature explicitly requires it.
