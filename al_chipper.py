
fish = int(input("Enter the amount of fish ordered:"))
chips = int(input("Enter the amount of chips ordered:"))

order = (1*fish) + ( 1*chips)

vat = order * 0.09

order_without_vat = order - vat 

tota_profit = order_without_vat/2

print(f'Toatl profit is {round(tota_profit, 2)}')
print(f'Toatl vat is {round(vat, 2)}')