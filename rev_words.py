#reverse the words seperated with spaces
f = open('B-large-practice.in', 'r')
cases = int(f.readline())
back = open('words.out', 'w')
back.close()
i = 0
while i < cases:
    line = f.readline()
    list_words = line.split(' ')
    last_one = list_words.pop()
    list_words.append(last_one[:-1])
    rev_words = list_words[::-1]
    final = open('words.out', 'a')
    new_str = ''
    for j, items in enumerate(rev_words):
        if j == len(rev_words)-1:
            print(str(j)+"=="+str(len(rev_words)-1))
            new_str = new_str + items+"\n"
        else:
            new_str = new_str+items+" "
    final.write("Case #"+str(i+1)+": "+new_str)
    final.close()
    i += 1
f.close()

