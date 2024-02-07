# @@@ Dividend Yield Calculator @@@

# @@@ Vignesh kumaran @@@
# @@@ February 2024 @@@

sharesQty = int(input("Enter you Share Qty: "))
dividendPerShare = float(input("Enter Dividend Per Share: "))
beforeTax = sharesQty * dividendPerShare

def TenPercent():
    result = beforeTax * 0.1
    return result

def FifteenPercent():
    result = beforeTax * 0.15
    return result

def TwentyPercent():
    result = beforeTax * 0.2
    return result

def TwentyFivePercent():
    result = beforeTax * 0.25
    return result

def ThirtyPercent():
    result = beforeTax * 0.3
    return result

def dash():
    print('-'*50)

if(beforeTax > 5000):
    print("<<< You are under Tax >>>")
    choiceOfUser = int(input("Enter you tax range: [10%, 15%, 20%, 25%, 30%]: "))

    if (choiceOfUser==10 or choiceOfUser==15 or choiceOfUser==20 or choiceOfUser==25 or choiceOfUser==30) :
        match choiceOfUser:
            case 10:
                taxResult = TenPercent(); 
            case 15:
                taxResult = FifteenPercent()
            case 20:
                taxResult = TwentyPercent()
            case 25:
                taxResult = TwentyFivePercent()
            case 30:
                taxResult = ThirtyPercent()

        afterTax = beforeTax - taxResult
    else:
        print("Enter a Valid Tax Range 10%, 15%, 20%, 25%, 30%")
else:
    print("Tax-Free!")
    afterTax = beforeTax

dash()
print(' '*20 + "Final Dividend")
dash()
print("Before Tax: " + str(beforeTax) + "\nAfter Tax: " + str(afterTax))
dash()
