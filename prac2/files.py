out_file=open("name.txt",'w')
names=input('What is your name：')
print(names,file=out_file) #这个是什么意思
out_file.close()

out_file=open("name.txt",'r')
print('Your name is {}'.format(names))
out_file.close()

total=0
in_file=open('number','r')
for i in range(2):
    text = in_file.readline()
    total=total+int(text)
print("The total is: ",total)
in_file.close()

