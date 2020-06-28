price=1000
good_credit=False
if good_credit:
    price=price-(price*(10/100))
else:
    price=price-(price*(20/100))
print('house sold on',price)

high_income=True
credit=True
criminal=False
# AND =logical operator for BOTH) and OR=(logical opeartor for atleast ONE)
# NOT =(logical opearator for inverse negative value)
if high_income and credit and not criminal:
    print('eligible for loan!!')