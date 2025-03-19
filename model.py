import numpy as np

def calculate_budget():
    income = 5000
    expenses = np.random.randint(500, 2000, size=5)
    total_expenses = sum(expenses)
    savings = income - total_expenses
    return {
        "income": income,
        "expenses": expenses.tolist(),
        "total_expenses": total_expenses,
        "savings": savings
    }
Model. Py