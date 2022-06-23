x = list()
s = input("請輸入字串(ok結束):")
while s != "ok":    
    x.append(s)
    s = input("請輸入字串(ok結束):")
print(x)
def longestCommonPrefix(strs):
    a = min(strs)
    b = max(strs)
    for i in range(min(len(a),len(b))):
        if a[i] != b[i]:
            return a[:i]
    return a if a else ""
print(longestCommonPrefix(x))