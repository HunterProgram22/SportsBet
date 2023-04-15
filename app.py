from flask import Flask, render_template
import requests

from odds import get_odds

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/odds')
def odds():
    # Make request to API
    odds_data = get_odds()

    # Extract odds data from JSON response
    # odds_data = response.json()

    # Pass odds data to template
    return render_template('odds.html', odds=odds_data)


if __name__ == '__main__':
    app.run(debug=True)
