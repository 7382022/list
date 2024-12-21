customerPaid=4.00
CustomerPurchase=3
balanceAmount=0

def PurcahseCalculator(customerPaid,CustomerPurchase):
    return(customerPaid-CustomerPurchase)


balanceAmount = PurcahseCalculator(customerPaid,CustomerPurchase)

print("Vishal Purchased : ",CustomerPurchase)
print("Vishal Paid : ",customerPaid)
print("Vishal Balance : ", balanceAmount)


print("Vishal bought ice cream for: ", CustomerPurchase ,"but he paid to shop keeper",customerPaid,". Shop Keeper returned balance amount ",balanceAmount)