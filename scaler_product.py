#find the minimum scaler product of two vectors
f = open("A-large-practice.in", 'r')
cases = f.readline()
ans_file = open('vec.out', 'w')
ans_file.close()
i = 0
while i < int(cases):
    cos = int(f.readline())
    x = f.readline().split(' ')
    y = f.readline().split(' ')
    xs = map(int, x)
    ys = map(int, y)
    xs.sort()
    ys.sort()
    ysr = ys[::-1]
    ans = 0
    for j,k in enumerate(xs):
        for l,m in enumerate(ysr):
            if j == l:
                ans += k*m
                break
            else:
                continue
    output = open('vec.out', 'a')
    output.write("Case #"+str(i+1)+": "+str(ans)+"\n")
    output.close()
    i += 1
f.close()



