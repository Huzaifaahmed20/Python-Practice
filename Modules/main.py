from calculations import calculations

tax_for_this_order = calculations.calculateTax(sales_total=101.37, tax_rate=.05)

print(tax_for_this_order)