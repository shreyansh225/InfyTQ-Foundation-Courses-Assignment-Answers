def validate_credit_card_number(card_number):
    numStr=str(card_number)
    to=0
    a=0
    tu=0
    for i in range(len(numStr)):
        if i%2==0:
            dou=(int(numStr[i])*2)
            
            if(len(str(dou))>=1):
                for i in str(dou):
                    tu+=int(i)
                to=to+tu
                tu=0
            else:
                to=to+int(dou)
        else:
            a=a+(int(numStr[i]))
    if (a+to)%10==0:
        return True
    else:
        return False
    #start writing your code here

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
    
# credit card number is invalid
