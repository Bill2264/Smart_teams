from datetime import datetime, timedelta
import json

class Calculations:
    def __init__(self, filename="expenses.json"):
        self.expenses = [] 
        self.weekly_budget = None
        self.filename = filename
        self.load_data()

    
    def add_expense(self, date, amount, category):
        self.expenses.append((date, amount, category))
        self.save_data()
        return self.budget_warning()  

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_data()


    def edit_expense(self, index, date, amount, category):
        if 0 <= index < len(self.expenses):
            self.expenses[index] = (date, amount, category)
            self.save_data()
            return self.budget_warning()  
        return None

    
    def get_total(self):
        total = 0
        for exp in self.expenses:
            try:
                total += float(exp[1])
            except ValueError:
                pass
        return total

    def get_all(self):
        return self.expenses

   
    def set_weekly_budget(self, amount):
        self.weekly_budget = float(amount)
        self.save_data()

    def get_weekly_total(self):
        now = datetime.now()
        week_start = now - timedelta(days=now.weekday())
        week_total = 0

        for exp in self.expenses:
            try:
                date_obj = datetime.strptime(exp[0], "%d-%m-%Y")
                if date_obj >= week_start:
                    week_total += float(exp[1])
            except:
                pass
        return week_total

    def budget_warning(self):
        if self.weekly_budget is not None:
            week_total = self.get_weekly_total()
            if week_total > self.weekly_budget:
                return "\n\nWeekly budget exceeded!"
            elif week_total >= 0.9 * self.weekly_budget:
                return "\n\nWarning: You are nearing your weekly budget!"
        return None

    # Persistent storage
    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({
                "expenses": self.expenses,
                "weekly_budget": self.weekly_budget
            }, f)

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.expenses = data.get("expenses", [])
                self.weekly_budget = data.get("weekly_budget", None)
        except FileNotFoundError:
            self.expenses = []
            self.weekly_budget = None
