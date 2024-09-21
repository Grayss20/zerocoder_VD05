from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        "nav1": "nav-link active",
        "nav2": "nav-link"
    }
    return render_template('home.html', **context)


@app.route('/about/')
def about():
    context = {
        "nav1": "nav-link",
        "nav2": "nav-link active"
    }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run()