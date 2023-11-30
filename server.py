from flask import Flask, render_template, url_for,redirect
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homePage.html")

@app.route("/aboutus")
def about():
    return render_template("aboutUs.html")

@app.route("/services")
def services():
    return render_template("servicePage.html")

@app.route("/careers")
def careers():
    return render_template()

@app.route("/contactUs")
def contact():
    return render_template("contactPage.html")



if __name__ == "__main__":
    app.run(debug=True)