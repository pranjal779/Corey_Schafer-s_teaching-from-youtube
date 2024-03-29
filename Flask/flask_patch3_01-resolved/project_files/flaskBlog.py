from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = '8a75aabe4c8406d7eaa09e5c5671002d'

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
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
