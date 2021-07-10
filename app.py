from flask import Flask, abort
from flask import render_template
from data import tours, departures

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def dep(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html', id=id)


@app.route('/data/')
def show_data():
    return render_template('data.html', data=tours)


@app.route('/data/departures/<departure>')
def show_deps(departure):
    new_data = {i: tours[i] for i in tours.keys() if tours[i]['departure'] == departure}
    if new_data == {}:
        return abort(404)
    rus_departure = departures[departure]
    return render_template('dep_data.html', departure=rus_departure, data=new_data)


@app.route('/data/tours/<int:id>/')
def show_tour(id):
    if not id in tours.keys():
        abort(404)
    night_str = str(tours[id]['nights'])
    if int(night_str) % 100 in range(5, 21):
        night_str = night_str + ' ночей'
    elif (int(night_str) % 10 == 1):
        night_str = night_str + ' ночь'
    else:
        night_str = night_str + ' ночи'
    return render_template('tour_data.html', tour=tours[id], nights=night_str)


if __name__ == '__main__':
    app.run()
