# class representing a rental property
class RentalProperty:
    def __init__(self, rental_income, laundry_income,
                 storage_income, tax, insurance,
                 utilities, hoa, vacancy,
                 repairs, capital_exchange, management,
                 mortgage_costs, apr):
        # Create the RentalProperty object with monthly inputs
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        self.expenses = {
            'tax': tax,
            'insurance': insurance,
            'utilities': utilities,
            'hoa': hoa,
            'vacancy': vacancy,
            'repairs': repairs,
            'capital_exchange': capital_exchange,
            'management': management,
            'mortgage_costs': mortgage_costs
        }
        self.apr = apr

    # Calculate the net cash flow of the property on an annual basis
    def calculate_cash_flow(self):
        total_income = 12 * (self.rental_income +
                             self.laundry_income +
                             self.storage_income)
        total_expenses = 12 * sum(self.expenses.values())
        monthly_interest = (self.apr / 100) * self.expenses['mortgage_costs']
        total_expenses += 12 * monthly_interest
        return total_income - total_expenses

    # Calculate and return the Return on Investment (ROI) as an annual percentage
    def calculate_roi(self, initial_investment):
        cash_flow = self.calculate_cash_flow()
        return (cash_flow / initial_investment) * 100


# Function to get user input for monthly details of the rental property
def floatput(prompt):
    while True:
        user_input = input(prompt)
        if user_input.replace('.', '', 1).isdigit():
            return float(user_input)
        else:
            print("Invalid input. Please enter a valid number.")


# Function to get user input for monthly details of the rental property
def user_input():
    print("Please provide monthly details for your rental property:")

    rental_income = floatput("Monthly rental income: $")
    laundry_income = floatput("Monthly laundry income: $")
    storage_income = floatput("Monthly storage income: $")
    tax = floatput("Monthly property tax: $")
    insurance = floatput("Monthly insurance cost: $")
    utilities = floatput("Monthly utilities cost: $")
    hoa = floatput("Monthly HOA (Homeowners Association) fees: $")
    vacancy = floatput("Estimated monthly vacancy costs: $")
    repairs = floatput("Estimated monthly repairs and maintenance costs: $")
    capital_exchange = floatput("Monthly capital exchange costs: $")
    management = floatput("Monthly property management fees: $")
    mortgage_costs = floatput("Monthly mortgage costs: $")
    apr = floatput("Mortgage APR (Annual Percentage Rate): %")

    return (rental_income, laundry_income, storage_income, tax, insurance,
            utilities, hoa, vacancy, repairs, capital_exchange, management,
            mortgage_costs, apr)


# Main program execution
def main():
    # Get user inputs with input validation, create a RentalProperty object,
    # calculate ROI, and print the result
    user_inputs = user_input()

    initial_investment = 0
    while initial_investment <= 0:
        user_input = input("Enter your initial investment in the property: $")
        if user_input.replace('.', '', 1).isdigit():
            initial_investment = float(user_input)
            if initial_investment <= 0:
                print("Invalid input. Please enter a positive dollar amount.")
        else:
            print("Invalid input. Please enter a positive dollar amount.")

    property1 = RentalProperty(*user_inputs)
    roi_property1 = property1.calculate_roi(initial_investment)

    print(f"\nAnnual Return on Investment (ROI) for your property: {roi_property1:.2f}%")

main()