from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Pranjal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '1/20/2023'
    },
    {
        'author': 'Ram',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '1/20/2023'
    }
]


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
