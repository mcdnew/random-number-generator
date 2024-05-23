from flask import Flask, render_template, request
import random
import datetime
import os

app = Flask(__name__)

def generate_random_date(start_date, end_date, start_hour=9, end_hour=20):
    days = (end_date - start_date).days
    random_day = start_date + datetime.timedelta(days=random.randint(0, days))

    # Ensure the day is a weekday
    while random_day.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        random_day += datetime.timedelta(days=1)

    # Generate random hour and minute within the specified range
    random_hour = random.randint(start_hour, end_hour - 1)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    return datetime.datetime(random_day.year, random_day.month, random_day.day, random_hour, random_minute,
                             random_second)

@app.route('/', methods=['GET', 'POST'])
def index():
    dates = []
    if request.method == 'POST':
        num_dates = int(request.form['num_dates'])
        start_date_input = request.form['start_date']
        end_date_input = request.form['end_date']
        
        start_date = datetime.datetime.strptime(start_date_input, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date_input, '%Y-%m-%d')
        
        for _ in range(num_dates):
            dates.append(generate_random_date(start_date, end_date))

    return render_template('index.html', dates=dates)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

