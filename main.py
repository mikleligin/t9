import codecs
def clear(path):
    dic = []
    que = []
    dickclear = []
    while True:
        r = path.readline().replace('\r', '')
        if not r:
            break
        dic.append(r)
    for i in range(len(dic)):
        g = dic[i].replace('\n', '')
        dickclear.append(g)
    return dickclear

path1 = codecs.open("dictionary.txt", encoding='utf-8')
path2 = codecs.open("queries.txt", encoding='utf-8')
dic = clear(path1)
que = clear(path2)
t9 = codecs.open('t9.txt','w',encoding='utf-8')
print(que)
for xy in range(0,len(dic)):
    worddic = []
    dictword = dic[xy]

    # Берём слово из дикт и разбиваем на буквы
    for x in range(0, len(str(dictword))):
        worddic.append(dictword[x])
    for i in range(0, len(que)):
        wordque = []
        count = 0
        notcount = 0
        #берем слово из неправильных слов и разбиваем на буквы
        for j in range(len(que[i])):
            wordque.append(que[i][j])
            #Сравниваем буквы слова из словаря с неправильными
        for l in range(len(worddic)):
            for l2 in range(len(wordque)):
                if wordque[l2] == worddic[l]:
                    count+=1
        #смотрим количество несовпадений
        for i2 in range (0, len(worddic)):
            if len(worddic) != len(wordque):
                if i2 < len(worddic)-1 and i2<len(wordque)-1:
                    if worddic[i2] != wordque[i2]:
                        notcount+=1
                else:
                    notcount+=1
            else:
                if i2 < len(worddic):
                    if worddic[i2] != wordque[i2]:
                        notcount+=1
        #print(worddic)

        if (count == len(wordque) or count >= len(wordque)-2) and len(worddic)-len(wordque)<3 and count!=0 and count>notcount and len(wordque)<=len(worddic):
            if worddic:
                dc = ''
                qe = ''
                for m in range(len(worddic)):
                    dc+=worddic[m]
                for o in range (len(wordque)):
                    qe+=wordque[o]
                if len(worddic)-notcount != 0:

                    t9.writelines(f"{qe} {len(worddic)-notcount} {dic[xy]} \n")
                    print(f"{qe} {len(worddic)-notcount} {dic[xy]} \n-= count {count} notcount {notcount}=-")
                else:
                    t9.writelines(f"{qe} {count} {dic[xy]} \n")
                    print(f"{qe} {count} {dic[xy]}")

            else:
                qe = ''
                for o in range (len(wordque)):
                    qe+=wordque[o]
               # print(f'слова {qe} нет в словаре')
        #print(count)
t9.close()
