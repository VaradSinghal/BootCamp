name=str(input("Enter name"))
amount=int(input("Enetr the amount: "))
q=int(input("Enter the quantity"))
disc=float(input("Enter the disc%: "))
p=amount*q
final=p-(disc*p/100)
print(f"Name: {name} Cost: {p} Discount%: {disc}  Final: {final}")