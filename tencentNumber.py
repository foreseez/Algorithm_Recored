t = input()
num = []
for i in range(int(t)):
    n = input("length is    :")
    s = list(input())
    if len(s) != int(n):
        print("Error length please input again!")

    if s[0] == '8':
        size = len(s)
        if size >= 11:
            print("YES")
        else:
            print("NO")

    else:
        ma = -1
        sz = len(s)
        for i in range(sz):
            if(s[i] == '8'):
                ma = i
                break

        if (ma == -1 or  sz-ma <11):
            print("NO")
        else:
            print("YES")
