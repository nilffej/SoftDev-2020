# Jeff Lin
# SoftDev PD 9
# K08 Lemme Flask You Smp'n
# 2019-09-19

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Main page loaded") # Prints out something on load/reload in console
    return "This is the main page!"

@app.route("/goodbye")
def goodbye_world():
    print("Goodbye page loaded")
    return "This is a different page..."

@app.route("/spooky")
def spook_world():
    print("Spooky page loaded")
    return "BOO!"

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
