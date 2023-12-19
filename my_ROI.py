# Define a class representing a rental property
class RentalProperty:
    def __init__(self, monthly_rental_income, monthly_laundry_income,
                 monthly_storage_income,monthly_tax, monthly_insurance, 
                 monthly_utilities, monthly_hoa, monthly_vacancy, 
                 monthly_repairs, monthly_capital_exchange, monthly_management, 
                 monthly_mortgage_costs):
        # Initialize the RentalProperty object with provided monthly inputs
        self.monthly_rental_income = monthly_rental_income
        self.monthly_laundry_income = monthly_laundry_income
        self.monthly_storage_income = monthly_storage_income
        self.monthly_expenses = {
            'tax': monthly_tax,
            'insurance': monthly_insurance,
            'utilities': monthly_utilities,
            'hoa': monthly_hoa,
            'vacancy': monthly_vacancy,
            'repairs': monthly_repairs,
            'capital_exchange': monthly_capital_exchange,
            'management': monthly_management,
            'mortgage_costs': monthly_mortgage_costs
        }

    # Calculate the net cash flow of the property on an annual basis
    def calculate_cash_flow(self):
        total_income = 12 * (self.monthly_rental_income + 
                             self.monthly_laundry_income + 
                             self.monthly_storage_income)
        total_expenses = 12 * sum(self.monthly_expenses.values())
        return total_income - total_expenses

    # Calculate and return the Return on Investment (ROI) as an annual percentage
    def calculate_roi(self, initial_investment):
        cash_flow = self.calculate_cash_flow()
        return (cash_flow / initial_investment) * 100


# Function to get user input for monthly details of the rental property
def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.replace('.', '', 1).isdigit():
            return float(user_input)
        else:
            print("Invalid input. Please enter a valid number.")


# Function to get user input for monthly details of the rental property
def get_user_input():
    print("Please provide monthly details for your rental property:")

    monthly_rental_income = get_float_input("Monthly rental income: $")
    monthly_laundry_income = get_float_input("Monthly laundry income: $")
    monthly_storage_income = get_float_input("Monthly storage income: $")
    monthly_tax = get_float_input("Monthly property tax: $")
    monthly_insurance = get_float_input("Monthly insurance cost: $")
    monthly_utilities = get_float_input("Monthly utilities cost: $")
    monthly_hoa = get_float_input("Monthly HOA (Homeowners Association) fees: $")
    monthly_vacancy = get_float_input("Estimated monthly vacancy costs: $")
    monthly_repairs = get_float_input("Estimated monthly repairs and maintenance costs: $")
    monthly_capital_exchange = get_float_input("Monthly capital exchange costs: $")
    monthly_management = get_float_input("Monthly property management fees: $")
    monthly_mortgage_costs = get_float_input("Monthly mortgage costs: $")

    return (monthly_rental_income, monthly_laundry_income, monthly_storage_income,
            monthly_tax, monthly_insurance, monthly_utilities, monthly_hoa,
              monthly_vacancy, monthly_repairs, monthly_capital_exchange, 
              monthly_management, monthly_mortgage_costs)


# Main program execution
def main():
    # Get user inputs with input validation, create a RentalProperty object,
    # calculate ROI, and print the result
    user_inputs = get_user_input()

    initial_investment = 0
    while initial_investment <= 0:
        user_input = input("Enter your initial investment in the property: $")
        if user_input.replace('.', '', 1).isdigit():
            initial_investment = float(user_input)
            if initial_investment <= 0:
                print("Please enter a positive value for the initial investment.")
        else:
            print("Invalid input. Please enter a valid number for the initial investment.")

    property1 = RentalProperty(*user_inputs)
    roi_property1 = property1.calculate_roi(initial_investment)

    print(f"\nAnnual Return on Investment (ROI) for your property: {roi_property1:.2f}%")

main()
