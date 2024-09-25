u=int(input("ENTER UNIT CONSUMED DURING THE PERIOD="))
if u<50:
    amt=(u*2.60)+25
elif u<100:    
    amt=130+((u-50)*3.25)+35
elif u<200:
    amt=(130+162.50)+((u-100)+5.25)+50
else:
    amt=(130+162.50+526)+((u-200)*8.25)+75
print("TOTAL ELECTRICITY BILL AMOUNT=",amt)    
    
