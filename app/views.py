from app import app

# Return the main view
@app.route("/")
def main():
    return "Hello, Shane!"
