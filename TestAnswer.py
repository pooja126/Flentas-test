a = input()
ans = []
for i in range(a):
    b = raw_input()
    c = raw_input()
    if (b in c) or (b[::-1] in c):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print i