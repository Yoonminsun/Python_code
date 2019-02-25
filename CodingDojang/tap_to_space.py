f=open('./source.txt','r')

source = f.read()
f.close()
f=open('./source.txt','w')
f.write(source.replace("\t","    "))
f.close()