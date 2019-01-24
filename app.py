from flask import Flask, render_template

import api_wrapper

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main_page():
    restaurants = api_wrapper.RESTAURANTS
    available_ingreds = api_wrapper.get_food_items_v2()

    return render_template('index.html', restaurants=sorted(restaurants.keys()), available_ingreds=available_ingreds)


@app.route('/add_row')
def add_row():
    pass


if __name__ == '__main__':
    app.run()


