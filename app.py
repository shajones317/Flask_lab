from flask import Flask, render_template                                   # import flask framework

app = Flask(__name__)                                                      # create an app instance

@app.route("/")                                                            # use the home url
def hello():                                                               # method called hello
    return render_template("index.html")                                                 # returns "hello world"

if __name__ == "__main__":                                                 # when running python app.py
    app.run(debug=True)                                                              # run the flask appS