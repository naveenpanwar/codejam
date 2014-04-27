#alien languauge
f = open("A-small-practice.in", 'r')
inputs = f.readline()
inputs_int = map(int,inputs.split(' '))
i,j = 0,0
words = [] #list of existed words
while i < inputs_int[1]:
    words.append(f.readline()[:-1])
    i += 1
matches = [] #list of given combinations
while j < inputs_int[-1]:
    matches.append(f.readline()[:-1])
    j+=1

def match(a , b):
    total = 0
    for tick in a:
        for pick in b:
            if tick == pick:
                total += 1
    return total

def add_letter(items, sections, key, point, last):
    for m, l in enumerate(items):
        for n in sections:
            if last == True:
                n = n + key[:point]+ l +key[point+1:]
            else:
                n = n + key[:point] + l
            try:
                sections[m] = n
            except IndexError:
                sections.append(n)
    return sections

def write_in_file(k,words, sections):
    o = open('alien.out', 'a')
    o.write("Case #"+str(k+1)+": "+str(match(words, sections))+'\n')
    o.close()

o = open("alien.out", 'w')
o.close()

for k,test in enumerate(matches): #looping over the combinations string
    catches = dict()
    subject = []
    key = ''
    while True:
        a = test.find('(')
        b = test.find(')')
        if a == -1:                #if no tests e.g. (nqxb) found
            key = key+test
            catches[key]=subject
            stop = len(catches[key])
            sections = []
            if stop == 0:
                sections.append(key)
                write_in_file(k, words, sections)
            else:
                for z,items in enumerate(catches[key]):     #looping over list of items in dictonary for key
                    point = key.find('.')
                    if len(sections) != 0:
                            if z == (stop-1):
                                last = True
                                add_letter(items, sections, key, point, last)
                                break
                            else:
                                last = False
                                add_letter(items, sections, key, point, last)
                    else:
                        new_str = ''
                        for l in items:         #looping over letters in items
                            new_str = key[:point]
                            sections.append(new_str+l)
                    key = key[point+1:]
                o = open('alien.out', 'a')
                o.write("Case #"+str(k+1)+": "+str(match(words, sections))+'\n')
                o.close()
            break
        key = key+test[:a]+'.'      #creating key like nwlr.bm.bh
        subject.append(test[a+1:b]) #filling the choices in arrar e.g. (nqxb)
        test = test[b+1:]           #shortening the test string nwlr(nqxb)bm(dgqw)bh -> bm(dgqw)bh
f.close()
