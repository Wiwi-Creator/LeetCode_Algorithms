
A = [6,8,1,2,3,7,7]
B = int(input("your coins : "))

def maxIceCream(costs, coins) :
#先進行排序,再進迴圈
    k = sorted(costs)
    count = 0
    for i in k :
        if  coins >= i : 
            coins = coins - i
            count = count + 1
        else :
            return count
    return  count 

print("You can buy " , maxIceCream(A , B) , "kinds of ice cream !")
