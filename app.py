from flask import Flask, render_template, request
import requests

from odds import get_odds

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/odds', methods=['GET', 'POST'])
def odds():
    if request.method == 'POST':
        # Get selected sport from form data
        selected_sport = request.form.get('sport')

        # Make request to API with selected sport
        odds_data = get_odds(selected_sport)

        # Pass odds data to template
        return render_template('odds.html', odds=odds_data)

    # Render initial form
    return render_template('odds.html')


if __name__ == '__main__':
    app.run(debug=True)
