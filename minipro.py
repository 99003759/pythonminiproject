import re
count=0
software=[]
lines=0
pattern=re.compile("software",re.IGNORECASE)
with open("input.txt",'rt') as file_inf:
    for file_lin in file_inf:
        lines+=1
        if pattern.search(file_lin)!=None:
            software.append((lines,file_lin.rstrip('\n')))
    for answer in software:
        count+=1
        #print(answer[1])
    #print("count=",count) 
        with open("software.txt",'a') as file_ans:
            file_ans.writelines(str(count)+' :')
            file_ans.writelines(answer[1]+'\n')
