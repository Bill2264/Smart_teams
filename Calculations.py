class Calculations:
    def __init__(self):
        self.expenses = [] 

    def add_expense(self, date, amount, category, description):
       
        self.expenses.append((date, amount, category, description))

    def remove_expense(self, index):
        
        if 0 <= index < len(self.expenses):
            del self.expenses[index]

    def edit_expense(self, index, date, amount, category, description):
        
        if 0 <= index < len(self.expenses):
            self.expenses[index] = (date, amount, category, description)

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
