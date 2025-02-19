st.sidebar.title("📖 ReadMe - Loader Crane TCO App")
st.sidebar.info("""
### How to Use This App:
1️⃣ Enter the truck and crane costs, fuel price, maintenance, and other inputs.  
2️⃣ Click **"Calculate TCO"** to see the total cost of ownership.  
3️⃣ The app will show **Annual Costs, Break-even Point, and a Chart**.  
4️⃣ Adjust inputs to compare different scenarios.  

### Key Features:
✅ Calculates **Total Cost of Ownership (TCO)**  
✅ Estimates **Break-even point**  
✅ Visualizes **Cost vs Revenue** over time  

👨‍💻 **Developed using Python & Streamlit**  
📧 Contact: *your_email@example.com*  
""")

import streamlit as st

class LoaderCraneTCO:
    def __init__(self, truck_cost, crane_cost, installation_cost, fuel_cost_per_l, fuel_consumption,
                 annual_km, maintenance_cost, operator_salary, insurance_cost, tax_cost,
                 loan_interest_rate, loan_term, resale_value, years, revenue_per_year):
        self.truck_cost = truck_cost
        self.crane_cost = crane_cost
        self.installation_cost = installation_cost
        self.fuel_cost_per_l = fuel_cost_per_l
        self.fuel_consumption = fuel_consumption  # L per km
        self.annual_km = annual_km
        self.maintenance_cost = maintenance_cost
        self.operator_salary = operator_salary
        self.insurance_cost = insurance_cost
        self.tax_cost = tax_cost
        self.loan_interest_rate = loan_interest_rate / 100
        self.loan_term = loan_term
        self.resale_value = resale_value
        self.years = years
        self.revenue_per_year = revenue_per_year

    def calculate_annual_fuel_cost(self):
        return self.fuel_cost_per_l * self.fuel_consumption * self.annual_km

    def calculate_depreciation(self):
        total_cost = self.truck_cost + self.crane_cost + self.installation_cost
        return (total_cost - self.resale_value) / self.years

    def calculate_loan_payment(self):
        total_cost = self.truck_cost + self.crane_cost + self.installation_cost
        if self.loan_interest_rate == 0:
            return total_cost / self.loan_term
        monthly_rate = self.loan_interest_rate / 12
        months = self.loan_term * 12
        return (total_cost * monthly_rate) / (1 - (1 + monthly_rate) ** -months) * 12

    def calculate_annual_costs(self):
        fuel_cost = self.calculate_annual_fuel_cost()
        depreciation = self.calculate_depreciation()
        loan_payment = self.calculate_loan_payment()
        total_annual_cost = (fuel_cost + self.maintenance_cost + self.operator_salary +
                             self.insurance_cost + self.tax_cost + depreciation + loan_payment)
        return total_annual_cost

    def calculate_tco(self):
        return self.calculate_annual_costs() * self.years

    def calculate_break_even_years(self):
        annual_profit = self.revenue_per_year - self.calculate_annual_costs()
        if annual_profit <= 0:
            return "Never (operating at a loss)"
        return round(self.calculate_tco() / annual_profit, 2)

# Streamlit UI
st.title("Loader Crane TCO Calculator")
st.write("Enter details below to calculate Total Cost of Ownership and Break-even Analysis")

truck_cost = st.number_input("Truck Purchase Price ($)", min_value=0.0, value=100000.0)
crane_cost = st.number_input("Crane Purchase Price ($)", min_value=0.0, value=50000.0)
installation_cost = st.number_input("Installation Cost ($)", min_value=0.0, value=10000.0)
fuel_cost_per_l = st.number_input("Fuel Cost per Liter ($)", min_value=0.0, value=1.5)
fuel_consumption = st.number_input("Fuel Consumption (L/km)", min_value=0.0, value=0.3)
annual_km = annual_km = st.slider("Annual Distance Driven (km)", min_value=10000, max_value=100000, value=30000, step=1000)
maintenance_cost = st.number_input("Annual Maintenance Cost ($)", min_value=0.0, value=5000.0)
operator_salary = st.number_input("Operator Annual Salary ($)", min_value=0.0, value=40000.0)
insurance_cost = st.number_input("Annual Insurance Cost ($)", min_value=0.0, value=5000.0)
tax_cost = st.number_input("Annual Tax & Registration Cost ($)", min_value=0.0, value=2000.0)
loan_interest_rate = st.number_input("Loan Interest Rate (%)", min_value=0.0, value=5.0)
loan_term = st.number_input("Loan Term (Years)", min_value=1, value=5)
resale_value = st.number_input("Estimated Resale Value ($)", min_value=0.0, value=30000.0)
years = st.number_input("Ownership Period (Years)", min_value=1, value=10)
revenue_per_year = st.number_input("Expected Annual Revenue ($)", min_value=0.0, value=120000.0)

if st.button("Calculate TCO"):  
    # Create the TCO Model
    tco_model = LoaderCraneTCO(truck_cost, crane_cost, installation_cost, fuel_cost_per_l, fuel_consumption,
                               annual_km, maintenance_cost, operator_salary, insurance_cost, tax_cost,
                               loan_interest_rate, loan_term, resale_value, years, revenue_per_year)

    # Display Results
    st.subheader("Results")
    st.write(f"**Total Cost of Ownership for {years} years:** ${tco_model.calculate_tco():,.2f}")
    st.write(f"**Annual Cost:** ${tco_model.calculate_annual_costs():,.2f}")
    st.write(f"**Annual Fuel Cost:** ${tco_model.calculate_annual_fuel_cost():,.2f}")
    st.write(f"**Annual Depreciation:** ${tco_model.calculate_depreciation():,.2f}")
    st.write(f"**Annual Loan Payment:** ${tco_model.calculate_loan_payment():,.2f}")
    st.write(f"**Break-even Point (Years):** {tco_model.calculate_break_even_years()}")

    # 📊 Add Chart Below (Only If Button is Clicked)
    import pandas as pd
    import matplotlib.pyplot as plt

    # Data for the chart
    years_range = list(range(1, years + 1))
    cumulative_costs = [tco_model.calculate_annual_costs() * year for year in years_range]
    cumulative_revenue = [revenue_per_year * year for year in years_range]

    # Create a DataFrame for Streamlit
    df = pd.DataFrame({
        "Years": years_range,
        "Cumulative Cost ($)": cumulative_costs,
        "Cumulative Revenue ($)": cumulative_revenue
    })

    # Plot in Streamlit
    st.subheader("📊 Cumulative Cost vs Revenue Over Time")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df["Years"], df["Cumulative Cost ($)"], label="Cumulative Cost ($)", linestyle="--", marker="o", color="red")
    ax.plot(df["Years"], df["Cumulative Revenue ($)"], label="Cumulative Revenue ($)", linestyle="-", marker="s", color="green")

    ax.set_xlabel("Years")
    ax.set_ylabel("Amount ($)")
    ax.set_title("Break-even Analysis")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)  # Display the chart in Streamlit
