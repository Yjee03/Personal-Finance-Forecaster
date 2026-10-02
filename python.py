import matplotlib.pyplot as plt

print("--- Personal Finance & Savings Forecaster (Visualized) ---")

# Step 1: Taking basic data from the user
P = float(input("Initial Amount (Rs): "))
PMT = float(input("Monthly Contribution (Rs): "))
R_inflation = float(input("Expected Inflation Rate (%): "))
T = int(input("Time Period in Years: "))

# Step 2: Taking custom scenario interest rates
print("\n--- Enter Expected Interest Rates for Scenarios ---")
rate_worst = float(input("Worst Case Interest Rate (%): "))
rate_average = float(input("Average Case Interest Rate (%): "))
rate_best = float(input("Best Case Interest Rate (%): "))

interest_scenarios = {
    "Worst Case": rate_worst,
    "Average Case": rate_average,
    "Best Case": rate_best
}

# Lists to store data for the graph
scenarios = []
nominal_values = []
real_values = []

print("\n--- Final Results for Your Scenarios ---")

# Step 3: Looping through scenarios and calculating
for scenario_name, R_nominal in interest_scenarios.items():
    
    r = (R_nominal / 100) / 12
    n = T * 12
    i = R_inflation / 100
    
    fv_initial = P * ((1 + r) ** n)
    fv_annuity = PMT * (((1 + r) ** n) - 1) / r
    total_nominal_fv = fv_initial + fv_annuity
    
    real_fv = total_nominal_fv / ((1 + i) ** T)
    
    # Saving data to the lists for plotting
    scenarios.append(scenario_name)
    nominal_values.append(total_nominal_fv)
    real_values.append(real_fv)
    
    print(f"\n[{scenario_name}] - Assuming {R_nominal}% Annual Interest:")
    print(f"  Nominal Value (Without Inflation): Rs {total_nominal_fv:,.2f}")
    print(f"  Real Value (Purchasing Power)    : Rs {real_fv:,.2f}")
    print("-" * 50)

# Step 4: Plotting the Bar Chart
x = range(len(scenarios))
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(8, 5))

# Creating bars for Nominal and Real values side-by-side
ax.bar([pos - width/2 for pos in x], nominal_values, width, label='Nominal Value (Without Inflation)', color='skyblue')
ax.bar([pos + width/2 for pos in x], real_values, width, label='Real Value (Adjusted for Inflation)', color='orange')

# Formatting the graph
ax.set_ylabel('Future Value (Rs)')
ax.set_title('Savings Forecast: Nominal vs Real Value Across Scenarios')
ax.set_xticks(x)
ax.set_xticklabels(scenarios)
ax.legend()

# Displaying the graph on screen
plt.tight_layout()
plt.show()