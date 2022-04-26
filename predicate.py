import os
import sys
import re

logtext = []

fileOpenName1 = open('D:\\dss\\predicte\\11.data', 'r', errors='ignore', encoding='utf-8')


def set_contact():
    predic = {}
    
    lines = fileOpenName1.readlines()
    for line in lines:
        i = 0
        
        if line == '\n' or line=='' :
                continue
        try:
                line1 = line.strip()
                print('원본 : '+ '\t'+  line1)
                
                line1 = line1.replace("kb.adams.ai/resource","kb.kt.com/exobrain/resource")
                line1 = line1.replace("kb.adams.ai/schema/property","kb.kt.com/exobrain/resource/property")
                
                print('변환 : '+ '\t'+  line1)
                
                # 제일 뒤에 데이타 가져오기
                mtext = line1.split('>')
                stext = mtext[-1]
                stext = stext.replace(" .", "")
                stext = stext.strip()
                stext = stext.replace("\"","")
                stext = stext.replace(" ","_")
                print(stext)
                
                # 앞에 <>안에 내용 가져오기
                murl = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line1)
                
                for str_link in murl:
                    print('변환2 : '+ '\t'+  str_link)
                    
                    if i == 0 :
                         strchange = str_link.split('/')
                         strtext = strchange[-1]
                         
                         print('실제 변화 데이타 : '+ '\t'+  str_link)
                         print('실제 변화 데이타 : '+ '\t'+  strtext)
                         i = i+1

                #dic에 키가 있는지 확인
                if strtext in predic.keys():
                    stext = predic[strtext]
                else:
                    predic[strtext] = stext
                    
                pretext = line1.replace(strtext,stext)
                print('최종 결과 : '+ '\t'+  pretext)       
                
                logtext.append(pretext)         
        except:
                print('ERROR'+ '\t'+  line1)
        
set_contact()

filePath = 'D:\\dss\\predicte\\end.data'

with open(filePath, 'w+') as lf:
    lf.write('\n'.join(logtext))  

lf.close()     

fileOpenName1.close() 