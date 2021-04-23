
#改編為可執行簡易程式
jewels = str(input("輸入符合內容 : "))
stones = str(input("輸入石頭質地 : "))

# LeetCode 作答區 :
def numJewelsInStones(jewels, stones) :
    sum = 0
    if len(jewels) == 0 or len(stones) == 0 :
        return 0
    jewels = set(jewels)
    for i in stones :
        if i in jewels :
            sum = sum + 1 
        
    return sum  
    
print("符合其成分 : " , numJewelsInStones(jewels , stones) "種")
