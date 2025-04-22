from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        subject = request.form["subject"]
        return render_template("thankyou.html", name=name, email=email,subject=subject, message=message)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
