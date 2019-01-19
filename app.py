from flask import Flask, render_template

import api_wrapper

app = Flask(__name__)
API_CREDS = api_wrapper.API("c6065fe5", "e02df01235e480620daf9a737a4d520a")

@app.route('/', methods=["GET"])
def main_page():
    restaurants = api_wrapper.RESTAURANTS
    available_ingreds = API_CREDS.get_food_items_v2()

    chosen_ingreds = [""] * 5

    return render_template('index.html', restaurants=sorted(restaurants.keys()), chosen_ingreds=chosen_ingreds)

@app.route('/add_row')
def add_row():
    pass


if __name__ == '__main__':
    app.run()


