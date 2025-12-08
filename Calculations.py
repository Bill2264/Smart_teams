from datetime import datetime, timedelta
class Calculations:
    def __init__(self):
        self.expenses = [] 
        self.weekly_budget = None

    def add_expense(self, date, amount, category, type):
       
        self.expenses.append((date, amount, category, type))

    def remove_expense(self, index):
        
        if 0 <= index < len(self.expenses):
            del self.expenses[index]

    def edit_expense(self, index, date, amount, category, type):
        
        if 0 <= index < len(self.expenses):
            self.expenses[index] = (date, amount, category, type)

    def get_total(self):
        
        total = 0
        for exp in self.expenses:
            try:
                total += float(exp[1])  # add the amount
            except ValueError:
                pass
        return total

    def get_all(self):
       
        return self.expenses
    

    def get_weekly_budget(self,amount):
        self.weekly_budget = float(amount)

    def get_weekly_total(self):
        now=datetime.now()
        week_start = now - timedelta(days=now.weekday())
        week_total = 0

        for exp in self.expenses:
            try:
                date_obj = datetime.strptime(exp[0], "%d-%m-%Y")
                date_obj >= week_start
                week_total += float(exp[1])
            except:
                pass
        return week_total
    
    def budget_warning(self):
        warning=[]

        if self.weekly_budget:
            week_total = self.get_weekly_total()
            if week_total > self.weekly_budget:
                warning.append("Weekly bduget exceeded")
        return warning

    
