from HomeBuying.get_info import Info
import yfinance as yf
from Finance_dashboard.data import buyer_info

class Wealth(Info):

    def __init__(self, buyer_data):
        self.monthly_income = {}
        self.monthly_stock = {}
        self.monthly_pay = {} 
        self.salary = {}
        self.savings = {}
        self.tax_bracket = {}
        self.grant_count = {}
        self.grant_value = {}
        self.rsu_vesting_perc = {}
        self.rsu_price = {}
        self.monthly_expenses = sum(self.expenses_data.values())
        for buyer in self.buyers:
            self.salary[buyer] = self.get_data('Salary',buyer,0)
            self.savings[buyer] = self.get_data('Savings',buyer,0)
            self.tax_bracket[buyer] = self.get_data('Tax_bracket_perc',buyer,23)/100
            self.rsu_vesting_perc[buyer] = self.get_data("Rsu_vesting_perc",buyer,0)/100
            self.grant_count[buyer] = self.get_data('Rsus',buyer,0)/self.get_data("Rsu_vesting_window",buyer,4)*self.get_data("Rsu_vesting_perc",buyer,25)
            if self.grant_count[buyer] !=0: 
                _ticker = yf.Ticker(self.get_data('Rsu_ticker',buyer, "None"))
                self.rsu_price[buyer] = _ticker.history(period="today")["Close"][0]
                self.grant_value[buyer] = self.grant_count[buyer]*self.rsu_price[buyer]
            else:
                self.grant_value[buyer] = 0
            self.monthly_values(buyer)
        self.combine_wealth()
        print("Monthly Total: ", self.monthly_all_total)
        print("Monthly Cash: " , self.monthly_income_total)
        print("Monthly Expenses: ", self.monthly_expenses)

    def monthly_values(self,buyer):
        self.monthly_income[buyer] = round(self.salary[buyer]/12*(1-self.tax_bracket[buyer]),2)
        self.monthly_stock[buyer] = round((self.grant_value[buyer]*(1-self.tax_bracket[buyer]))/12,2)
        self.monthly_pay[buyer] = round(self.monthly_income[buyer]+self.monthly_stock[buyer],2)
    
    def combine_wealth(self):
        self.monthly_income_total = sum(self.monthly_income.values())
        self.monthly_stock_total = sum(self.monthly_stock.values())
        self.savings_all = sum(self.savings.values())
        self.monthly_all_total = round(self.monthly_income_total + self.monthly_stock_total,2)

if __name__ == "__main__":
    wealth = Wealth(home_buying_yaml=r'C:\Users\ianla\Documents\GitHub\HomeBuying\Emilian.yaml')
    print("Savings", wealth.savings_all)