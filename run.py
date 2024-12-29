from threading import Thread
from app.routes import app

# Function to run the app
def run_app():
    app.run(host='0.0.0.0', port=5000)

# Start the app in a separate thread
Thread(target=run_app).start()