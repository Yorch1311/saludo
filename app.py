from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Do you want it?!"
@app.route("/index") 
if __name__ == "__main__":
    app.run()
