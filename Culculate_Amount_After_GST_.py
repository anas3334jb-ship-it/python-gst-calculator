# TOTAL AMOUNT WITH GST
price = float(input("Enter unit price: "))
quantity = float(input('Enter the quantity: '))
gst_rate = float(input('Enter GST rate (in %): '))

total_price = price * quantity
gst_amount = (total_price * gst_rate)/100
total_amount = total_price + gst_amount
print("Total Amount (including GST):", total_amount)
