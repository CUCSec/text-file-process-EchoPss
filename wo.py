count=0
with open(r'D:\python123\text-file-process-EchoPss\text-file-process\log_files\201811113018.log',encoding='utf8') as f:
    for line in f:
        str1=line.split('：')[2]
        str2=str1[:12]
        if str2=='201811113018':
            count+=1
print(count)