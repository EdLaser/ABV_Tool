from flask import Flask, render_template
from csv import DictReader

app = Flask(__name__, template_folder='./')

def read_csv():
    with open('emissions.csv', newline='') as csvfile:
        reader = DictReader(csvfile, delimiter=',')
        emissions = []
        for row in reader:
            print(row)
            emissions.append(row)
        emissions.reverse()
        
        return emissions


@app.route("/")
def dashboard():
    wanted = ['timestamp', 'duration', 'cpu_power', 'gpu_energy', 'ram_power', 'emissions_rate', 'energy_consumed']
    return render_template('dashboard.html', emissions=read_csv(), wanted=wanted)
