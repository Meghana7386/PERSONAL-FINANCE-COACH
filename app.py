from flask import Flask, render_template, request
import os
from models.budget_model import calculate_budget
from services.advice_generator import generate_advice

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    budget_data = calculate_budget()
    return render_template('dashboard.html', budget_data=budget_data)

@app.route('/goals')
def goals():
    advice = generate_advice()
    return render_template('goals.html', advice=advice)

if __name__ == '__main__':
    app.run(debug=True)