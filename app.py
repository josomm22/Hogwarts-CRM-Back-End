from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route("/")
def main():
    return "hello there"

if __name__ == "__main__":
    threading.Thread(target=app.run).start()
    time.sleep(0.5)