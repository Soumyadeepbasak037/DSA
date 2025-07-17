def one_digit(num):
    single_digit = ["zero'","one","two","three","four","five","six","seven","eight","nine"]
    return (single_digit[num])

def two_digit(num):
    tens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    others = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


    if(num<10):
        print(one_digit(num))
        return

    if(num<20):
        indx = num%10
        print(tens[indx])
        return

    if(num<100):
        indx = num//10
        print(others[indx-2],end=" ")
        
        if(num%10 != 0):
            indx = num%10
            print(one_digit(indx))
        return

    if(num<1000):
        indx = num//100
        print(one_digit(indx)," Hundred ",end= ' ')
        two_digit(num%100)
        return


two_digit()    
