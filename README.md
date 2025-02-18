Building a Total Cost of Ownership (TCO) model for a loader crane mounted on a truck requires considering a wide range of costs over the crane's lifespan.

Here's a breakdown of the costs to include and how to structure the model:
I. Cost Categories:
  A. Acquisition Costs:
1. Crane Purchase Price: The initial cost of the crane itself, including any base attachments.
2. Truck Modification/Reinforcement: Costs to prepare the truck chassis for crane mounting (e.g., frame reinforcement, outrigger installation, PTO installation).
3. Mounting and Installation: Labor and materials for mounting the crane on the truck.
4. Truck Purchase/Lease: Cost of the truck itself (if not already owned). Include depreciation or lease payments.
5. Delivery and Shipping: Costs to transport the crane and truck.
6. Taxes and Fees: Sales tax, registration fees, etc.
7. Customization costs – Any additional features, sensors, or special equipment.

  B. Operating Costs:
1. Fuel: Fuel consumption for both the truck and the crane's hydraulic system (if applicable). Consider idle time.
2. Hydraulic Oil: Cost of hydraulic fluid and periodic changes.
3. Maintenance (Preventive): Scheduled maintenance like inspections, lubrication, filter changes, hose replacements, etc. Factor in frequency and labor costs.
4. Repairs (Unscheduled): Budget for unexpected repairs due to breakdowns, wear and tear, or accidental damage. This is harder to predict, but historical data or industry averages can help.
5. Operator Wages: Cost of the crane operator's salary and benefits.
6. Insurance: Insurance premiums for the truck and crane.

  C. Ownership Costs:
1. Depreciation: The decrease in value of the crane and truck over time. Use a suitable depreciation method (e.g., straight-line, declining balance).
2. Interest on Loan (if applicable): Interest paid on financing for the crane and/or truck.
3. Taxes (Property/Usage): Annual taxes related to owning and operating the equipment.
4. Permits and Licenses: Any required permits or licenses for operating the crane and truck.
D. Disposal Costs:
1. Resale Value: Estimated value of the crane and truck at the end of their useful life. This can be a positive value, offsetting some costs.
2. Dismounting and Removal: Costs to remove the crane from the truck and dispose of both.
3. Environmental Disposal Fees: Costs associated with disposing of fluids, tires, etc., in an environmentally responsible manner.

II. Model Structure:
1. Spreadsheet Software: Microsoft Excel or Google Sheets are ideal for building this type of model.
2. Input Variables: Create cells for all the cost categories listed above. These will be the input variables. Be as detailed as possible (e.g., instead of just "Maintenance," have separate lines for "Oil Changes," "Filter Replacements," etc.).
3. Time Horizon: Define the lifespan of the crane and truck (e.g., 5 years, 10 years). This will determine how many periods the model covers.
4. Formulas: Use formulas to calculate costs over time. For example:
Annual Fuel Cost = (Annual Truck Mileage * Truck Fuel Consumption Rate * Fuel Price) + (Annual Crane Operating Hours * Crane Fuel Consumption Rate * Fuel Price)
Depreciation = (Initial Cost - Salvage Value) / Useful Life
5. Total Cost Calculation: Sum all the costs for each year and then calculate the cumulative total cost over the entire time horizon.
6. Sensitivity Analysis: This is crucial. Identify the variables that have the biggest impact on the TCO (e.g., fuel price, utilization rate, repair costs). Use scenarios or data tables to see how changes in these variables affect the overall cost.
7. Output: The model should output the following:
- Annual costs for each category.
- Cumulative total cost of ownership over the time horizon.
- Key metrics like cost per hour, cost per lift, etc. (if applicable).
- Sensitivity analysis results.

III. Additional Tips:
- Data Collection: Gather accurate data for your input variables. Use historical data from your own operations, manufacturer specifications, industry benchmarks, and expert opinions.
- Assumptions: Clearly state all assumptions made in your model.
- Regular Updates: Update your model periodically with actual cost data to refine its accuracy.
- Consider External Factors: Think about factors like inflation, technological advancements, and changes in regulations that might affect costs over time.
Use a Discount Rate: If you're comparing different options with different lifespans, use a discount rate to bring future costs to their present value. This allows for a more accurate comparison.

IV. Building the Model:
Step 1: Define Inputs
Create an Excel spreadsheet or a Python model with input variables like:
Purchase price of truck & crane
Fuel consumption (L/km or L/hr)
Annual mileage or operational hours
Maintenance cost per year
Operator wages
Insurance & registration fees
Loan/lease terms (interest rate, monthly payment, duration)
Expected resale value
Step 2: Calculate Annual Costs
Separate fixed and variable costs.
Sum fuel, maintenance, and labor for annual operating costs.
Include depreciation using straight-line or declining balance methods.
Step 3: Calculate Total Cost of Ownership (TCO)
TCO=∑(Fixed Costs+Operating Costs−Residual Value)\text{TCO} = \sum (\text{Fixed Costs} + \text{Operating Costs} - \text{Residual Value})
