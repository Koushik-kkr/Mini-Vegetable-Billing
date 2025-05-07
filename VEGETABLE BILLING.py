veg=['potato','tomato','carrot','beetroot']
quantity=[5,7,10,6]
price=[25,60,70,90]
sumP=0
sumT=0
sumC=0
sumB=0
sumtotal=0
while True:
    sum=0
    print(veg)
    print('1.BUY')
    print('2.REPORT')
    print('3.EXIT')
    first=int(input('CHOOSE AN OPTION '))
    if first ==1:
        item=input('ENTER WHAT DO YOU WANT ')
        if item in veg:
            quan=float(input('ENTER HOW MUCH DO YOU WANT '))
            idx=veg.index(item)
            if quan<=quantity[idx]:
                cost=quan*price[idx]
                print('PLEASE PAY',cost,'RUPEES')
                quantity[idx]=quantity[idx]-quan
                if item=='potato':
                    sumP=sumP+cost
                elif item=='tomato':
                    sumT=sumT+cost
                elif item=='carrot':
                    sumC=sumC+cost
                else:
                    sumB=sumB+cost
                sum=sum+cost
                sumtotal=sumtotal+cost
            else:
                print('OUT OF STOCK')    
        else:
            print('OUT OF STOCK')
    elif first==2:
            for k,v in zip(veg,quantity):
                print(k,v)
            print('TODAY TOTAL TOMATO REVENUE IS',sumT,'RUPEES')
            print('TODAY TOTAL POTATO REVENUE IS',sumP,'RUPEES')
            print('TODAY TOTAL CARROT REVENUE IS',sumC,'RUPEES')
            print('TODAY TOTAL BEETROOT REVENUE IS',sumB,'RUPEES')
            print('TODAY TOTAL TOMATO REVENUE IS',sumtotal,'RUPEES')
    elif first==3:
            print('THANKYOU FOR SHOOPING')
            break
        
