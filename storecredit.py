#codejam practice exercise storecredit depicts the problem of dealing with credits and buying stuff

import time
print(time.clock())
a = open('A-large-practice.in', 'r')
output = open('bill','w')
output.close()
def into_int(a):
    return int(a.readline())

cases = into_int(a)
i = 0
done = False
while i < cases:
    credit = into_int(a)
    n_items = into_int(a)
    items_list = a.readline().split(' ')
    items_int = map(int, items_list)
    for j,k in enumerate(items_int):
        for l,m in enumerate(items_int):
            if m >= credit:
                continue
            elif k + m == credit:
                if j == l:
                    continue
                output = open('bill', 'a')
                output.write("Case #"+str(i+1)+": "+str(j+1)+" "+str(l+1)+"\n")
                output.close()
                done = True
                break
        if done == True:
            done = False
            break
    i += 1
a.close()
print(time.clock())
