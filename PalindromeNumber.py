a = input("輸入一組數字 : ")
def isPalindrome(x) :
    s = str(x)
    rtl = ''
    for i in s :
        rtl =  i + rtl
    return s == rtl
print(a + "是否為迴文數 :" , isPalindrome(a))