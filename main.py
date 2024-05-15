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

# Steps
"""
So, let's say you have a frontend running in your browser at http://localhost:8080,
and its JavaScript is trying to communicate with a backend running at http://localhost (because don't specify a port, the browser will assume the default port 80).

Then, the browser will send an HTTP OPTOPNS request to the backend, and if the backend sends the appropriate headers authorizing the communication from this different origin (http://localhost:8080) then the browser will let the JavaScript in the frontend send its request to the backend.

To achieve this, the backend must have a list of "allowed origins".

In this case, it would have to include http://localhost:8080 for the frontend to work correctly.
"""
