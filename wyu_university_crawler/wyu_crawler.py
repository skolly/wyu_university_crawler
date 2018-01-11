# encoding=utf-8

import requests
from datetime import datetime
import json
import time

class Crawler_score:
    global url,data
    
    url = 'http://202.192.240.29'  #wyu新子系统网址

    
    data = {'account' : '',
             'pwd':'',
             'verifycode':''
            } # 发送的数据以及格式


    def __init__(self): 

        global account

        self.get_verify() 

        vercode = str(input("请输入验证码：")) #输入验证码
    
        account = str(input('请输入你的学号：')) #输入学号
    
        pwd = str(input('请输入你的密码：')) #输入密码


        # 写入data字典 
        data['verifycode'] = vercode #
    
        data['account'] = account 
    
        data['pwd'] = pwd 

        self.login_in() 

        self.get_score()

        self.data_processing()
        


    def login_in(self): #发送数据 登录子系统

        global session,headers
   
        login_url =  url + '/new/login' # 接收数据的网址
        
        headers = {'User-Agent':'Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
               (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'} # 修改请求头 防止ip被禁

        session = requests.session()  # 使用session()函数，自动更新cookies信息
     
        r = session.post(login_url,headers=headers,\
                cookies = requests.utils.dict_from_cookiejar(var_code.cookies),\
                data=data)
        
        time.sleep(3) # 友好操作

    def get_verify(self): #获取验证码图片

        global var_code
      
        verify_url = url + '/yzm?d=1512785249083' # 获取验证码的网址

        var_code = requests.get(verify_url) # 得到验证码
        
        time.sleep(3) # 友好操作


        with open( datetime.now().date().isoformat()+'.png','wb') as f: # 把验证码保存.txt文件
    
            f.write(var_code.content)
      
            f.close()


    def get_score(self): # 获取成绩  把成绩保存为.txt文件
        
        datas = {

        'xnxqdm':'201701',
        'page':'1',
        'rows':'20',
        'sort':'xnxqdm',
        'order':'asc'

            } # 获取2017年第一学期的成绩的数据
    
        get_score_url = url + '/xskccjxx!getDataList.action' #获得成绩网址
    
        score_html = session.post(get_score_url,headers=headers,\
                              
            cookies = requests.utils.dict_from_cookiejar(var_code.cookies),\
                              
            data=datas)


        
        with open( account+'.txt','wb') as f: # 把成绩保存为.txt文件,内容为json格式
        
            f.write(score_html.content)
        
            f.close()


        
    def data_processing(self): # 文件中的数据处理

    
        with open( account+'.txt','r',encoding = 'utf-8') as f:
    
            data = json.load(f) # 转换json格式为字典格式

            datas = data['rows'] # 获取list格式的成绩

            f.close()

    

        with open(account + '.txt','w',encoding = 'utf-8') as d:
    
            for i in  datas : # 遍历list 获取科目和成绩
        
                scores = ('wow~ ⊙o⊙成绩出来了   ' + i['kcmc'] \
                          
                     + ' : ' + i['zcj']+'\n')
                
                print (i['kcmc'] + ' : ' + i['zcj'])  # 此为验证成绩是否正确，可注释掉  
        
                d.write(scores)
            
        d.close()


Crawler_score()
                






 
