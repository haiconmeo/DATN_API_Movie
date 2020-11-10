import os
f  = open("file.txt",'w')
for i in os.listdir("../static/img"):
    f.write(i.split('.')[0]+'::'+i+"\n")
f.close()
    