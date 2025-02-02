f = open('perepis.txt', 'r')
ch = 0
for i in f:
    if int(i[-4:-1]) < 1978:
        print(i.split()[0])
        ch += 1
f.close()
print(ch)
