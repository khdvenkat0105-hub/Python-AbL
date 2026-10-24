#Retail Billing with Multiple Discount Rules(7th)
n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    print("Product", i + 1)
    price = float(input("Enter price: Rs. "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid product details")
    else:
        amount = price * quantity
        total = total + amount

print("Subtotal: Rs.", round(total, 2))

if total >= 5000:
    discount = total * 0.10
elif total >= 2000:
    discount = total * 0.05
else:
    discount = 0

tax = (total - discount) * 0.05
final_bill = total - discount + tax

print("Discount: Rs.", round(discount, 2))
print("Tax: Rs.", round(tax, 2))
print("Final bill: Rs.", round(final_bill, 2))
