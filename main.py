from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import secrets

app = Flask(__name__)
foo = secrets.token_urlsafe(16)

app.config['SECRET_KEY'] = foo
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_link = StringField('Cafe Location', validators=[DataRequired(), URL(message="No url!")])
    open_time = StringField('Opening Time e.g. 11AM', validators=[DataRequired()])
    close_time = StringField('Closening Time e.g. 3PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',
                                validators=[DataRequired()],
                                choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi_rating = SelectField('Wifi Strength Rating',
                              validators=[DataRequired()],
                              choices=["✘", "💪", "💪💪", "💪💪💪"])
    power_rating = SelectField('Power Socket Availability',
                               validators=[DataRequired()],
                               choices=["🔌", "🔌🔌", "🔌🔌🔌"])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            csv.writer(csv_file).writerow([form.data['cafe'],
                                          form.data['location_link'],
                                          form.data['open_time'],
                                          form.data['close_time'],
                                          form.data['coffee_rating'],
                                          form.data['wifi_rating'],
                                          form.data['power_rating']])
        print("done")
    else:
        print(form.errors)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
