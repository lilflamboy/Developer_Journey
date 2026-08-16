Price = float(input("Enter the price of the item: "))
Discount = int(input("Enter the discount percentage: "))
Discount_amount = (Price * Discount) / 100
Final_price = Price - Discount_amount

print(f"Discount amount: ₹{Discount_amount:.2f}")
print(f"Final price after discount: ₹{Final_price:.2f}")