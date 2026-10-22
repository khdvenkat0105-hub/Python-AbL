#Case-2 — Repeated Transaction Detection(28th)
ids = ["T101", "T102", "T103", "T101", "T104"]
amounts = [2000, 15000, 5000, 2000, 12000]
seen = []
print("Transaction Audit")
for i in range(len(ids)):
    print("ID:", ids[i], "Amount:", amounts[i])
    if ids[i] in seen:
        print("Warning: Duplicate transaction ID")
    else:
        seen.append(ids[i])
    if amounts[i] > 10000:
        print("Warning: Amount exceeds 10000")
print("Audit completed")