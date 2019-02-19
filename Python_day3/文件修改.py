# Author:GaoYuCai
#文件修改存入其他文件中
f=open("c:\\file.txt",'r')
f_new=open("c:\\file1.txt",'w')
for line  in  f:
    if "肆意的快乐等我去享受"  in  line:
        line=line.replace("肆意的快乐等我去享受","肆意的快乐等Alex去享受")
    f_new.write(line)
f.close()
f_new.close()