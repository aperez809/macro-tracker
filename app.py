from flask import Flask, render_template

import api_wrapper

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main_page():
    restaurants = api_wrapper.RESTAURANTS
    return render_template('index.html', restaurants=sorted(restaurants.keys()))


if __name__ == '__main__':
    app.run()


