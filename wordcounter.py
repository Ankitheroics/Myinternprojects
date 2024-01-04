
#paragraph to be
sentence= input("enter the sentence or paragraph \n")

sentence=sentence.replace(',', '').lower().split()
wc={}

for word in sentence:

    if word in wc.keys():
        wc[word] += 1


    else:

        wc[word]=1


print(wc)

