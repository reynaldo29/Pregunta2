import random
'''
///////////////////////////
creando el archivo txt
////////////////////////////
'''
f = open('bst.txt','w')
for i in  range(1000):
    x=(random.randrange(1,50000))
    f.write(str(x) + ' ')
f.close()





