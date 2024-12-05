taxable_income = float(input("Enter taxable income (₹): "))
tax = 0
if taxable_income > 1500000:
 tax += (taxable_income- 1500000) * 0.30
 taxable_income = 1500000
if taxable_income > 1200000:
 tax += (taxable_income - 1200000) * 0.20
 taxable_income = 1200000
if taxable_income > 900000:
 tax += (taxable_income - 900000) * 0.15
 taxable_income = 900000
if taxable_income > 600000:
 tax += (taxable_income - 600000) * 0.10
 taxable_income = 600000
if taxable_income > 300000:
 tax += (taxable_income - 300000) * 0.05

if taxable_income <= 700000:
 tax = 0
cess = tax * 0.04
total_tax_payable = tax + cess
print("\n--- Tax Breakdown ---")
print(f"Base Tax: ₹{tax:.2f}")
print(f"Health and Education Cess (4%): ₹{cess:.2f}")
print(f"Total Tax Payable: ₹{total_tax_payable:.2f}") 