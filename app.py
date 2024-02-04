from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    # Check if 'name' is in the query parameters, if not, use a default value
    name = request.args.get('name') if request.args.get('name') else "Hello World!"
    return render_template("about.html", aboutName=name)

if __name__ == "__main__":
    app.run(debug=True)
