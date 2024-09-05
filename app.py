from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def intro():
    return ("<h1>This is an introduction page</h1>")

@app.route("/homepage")
def get_homepage():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "<p>Hello World</p>"

@app.route("/goodbye")
def goodbye():
    x = create_title()
    return x

def create_title():
    return "<h1>This is a title created by the method create_title</h1>"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return "<h2>Contact us at contact@example.com</h2>"

@app.route("/services")
def services():
    return "<h3>List of Services:</h3><ul><li>Web Development</li><li>SEO</li><li>Marketing</li></ul>"

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/greet/<name>")
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route("/age/<int:age>")
def age_check(age):
    if age >= 18:
        return "<h2> You are eligible to vote!</h2>"
    else:
        return "<h2>Sorry, you are too young to vote.</h2>"

@app.route("/profile/<username>")
def profile(username):
    return f"<h1>Welcome to {username}'s profile page</h1>"

@app.route("/portfolio")
def portfolio():
    return "<h2>Here is the portfolio page.</h2>"

@app.route("/blog")
def blog():
    return "<h3>Latest blog post: Learning flask is fun!</h3>"

@app.route("/blog/<int:post_id>")
def blog_post(post_id):
    return f"<h3>Displaying blog post #{post_id}</h3>"

@app.route("/terms")
def terms():
    return "<p>These are the terms and conditions of the website.</p>"

@app.route("/privacy")
def privacy():
    return "<p>This is our privacy policy page.</p>"

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/shop")
def shop():
    return "<h2>Welcome to our shop!</h2>"

@app.route("/product/<int:product_id>")
def product(product_id):
    return f"<h3>Details for Product #{product_id}</h3>"

@app.route("/external")
def external():
    return "<a href='https://www.example.com'>Visit Example.com</a>"

if __name__ == "__main__":
    app.run(debug=True, port=8080)

