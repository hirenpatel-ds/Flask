from flask import Flask

# communicate with server and web application
app = Flask(__name__)  # Creating WSGI application which is a standard which will be communicate with server

# This decorator is binding with function. Decorator: 2 parameters 1. URL and 2. methods


@app.route("/")
def welcome():
    return "Hello World"

# We can define multiple routes

@app.route("/cls")
def cls():
    return "Hello Thank you for enrolling"


if __name__ == "__main__":
    app.run(debug=True)
