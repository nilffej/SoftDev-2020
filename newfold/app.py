from flask import Flask, render_template
app = Flask(__name__)

coll = [0,1,1,2,3,5,8]

@app.route("/")
def hello_world():
    print("Main page loaded") # Prints out something on load/reload in console
    return "New test page!"

@app.route("/my_foist_template")
def newpage():
    return render_template('site.html',
    foo = "foooo",
    collection= coll
    )

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
