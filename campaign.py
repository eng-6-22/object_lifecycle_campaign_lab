class Campaign:
    def __init__(self, budget):
        self.budget = float(budget)

    def set_revenue(self, revenue):
        self.revenue = revenue

    def set_customers_acquired(self, amount):
        self.customers_acquired = amount 

    def average_revenue_per_customer(self):
        return self.revenue/self.customers_acquired
    
    def profit(self):
        return self.revenue - self.budget

    def breakeven_customer_number(self):
        return self.profit()/self.average_revenue_per_customer()

    
    



