from fastapi import FastAPI

app = FastAPI()

# CORS (Cross-Origin Resource Sharing)
"""
CORS or "Cross-Origin Resource Sharing" refers to the situations when a frontend running in a browser has JavaScript code that communicates with a backend,
and the backend is in a different "origin" than the frontend
"""

# Origin
"""
An origin is the combination of protocol (http, https), domain (mayapp.com, localhost, localhost.tiangolo.com), and port (80, 443, 8080).

So, all these are different origins:
- http://localhost
- https://localhost
- http://localhost:8080

Even if they are all in localhost, they use different protocols or ports, so, they are different "origins".
"""
