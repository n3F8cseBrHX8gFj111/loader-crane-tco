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
        total_annual_cost = (fuel_cost + self.maint
