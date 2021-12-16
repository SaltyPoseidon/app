from flask import Flask
from flask import send_file
from flask import render_template
import pandas as pd
import matplotlib.pyplot as plt
import time

app = Flask(__name__)
links = {"Download" : "/download",
         "Pairplot" : "/pairplot",
         "Fair vs Pclass"  : "fair_vs_pclass",
         "PClass vs Sex" : "pclass_vs_sex"}

def render_index (image = None):
    return render_template("index.html", links=links, image = (image, image), code=time.time())

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", links=links)

@app.route('/download', methods=['GET'])
def download_data():
    return send_file("data/titanic_train.csv", as_attachment=True)

@app.route('/fair_vs_pclass', methods=['GET'])
def fair_vs_pclass():
    data = pd.read_csv ("data/titanic_train.csv")
    filtered_data = data.query('Fare < 200')
    x = list(data['Pclass'])
    y = list(data['Fare'])
    plt.boxplot(x, y)
    plt.savefig('static/tmp/fair_vs_pclass.png')
    return render_index("fair_vs_pclass.png")


# app.run()
