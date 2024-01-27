# __init__.py

from app import create_app

# Create the Flask app instance
app = create_app()

# Optionally, you can add initialization code here if needed.

# If you want to run the app when the package is directly executed
if __name__ == "__main__":
    app.run()
