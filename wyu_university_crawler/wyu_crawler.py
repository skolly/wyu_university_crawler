# encoding=utf-8

import requests
from datetime import datetime
import json
import time

class Crawler_score(object):

    #wyu新子系统网址
    url = 'http://202.192.240.29'  

    # 修改请求头 防止ip被禁
    headers = {'User-Agent':'Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
               (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'} 

    # 发送的数据以及格式  
    data = {'account' : '',
             'pwd':'',
             'verifycode':''
            } 

    #定义实例属性，初始化
    def __init__(self): 

        self.get_verify() 

        # 输入验证码
        vercode = str(input("请输入验证码：")) 

        # 输入学号 
        self.account = str(input('请输入你的学号：'))    

        #输入密码   
        pwd = str(input('请输入你的密码：'))  


        # 把数据保存在data中 
        self.data['verifycode'] = vercode 
    
        self.data['account'] = self.account 
    
        self.data['pwd'] = pwd 

        self.login_in()       
        

    # 登录子系统
    def login_in(self): 

        # 接收数据的网址
        login_url =  self.url + '/new/login' 

        # 使用session()函数，自动更新cookies信息
        self.session = requests.session()  

        # 使用POST方法，将data中的数据转换成cookies     
        r = self.session.post(login_url,headers=self.headers,\
             cookies = requests.utils.dict_from_cookiejar(self.var_code.cookies),\
                    data=self.data)

        # 友好操作
        time.sleep(1)

        self.get_score()
            

    # 获取验证码图片
    def get_verify(self): 

        # 获取验证码的网址
        verify_url = self.url + '/yzm?d=1512785249083' 

        # 得到验证码
        self.var_code = requests.get(verify_url) 

        # 把验证码保存为.png格式文件
        with open( datetime.now().date().isoformat()+'.png','wb') as f: 
    
            f.write(self.var_code.content)
      
            f.close()

    # 获取成绩  把成绩保存为.txt文件
    def get_score(self): 

        # 获取2017年第一学期的成绩的数据        
        datas = {

        'xnxqdm':'201701',
        'page':'1',
        'rows':'20',
        'sort':'xnxqdm',
        'order':'asc'

            } 

        # 获取成绩的网址    
        get_score_url = self.url + '/xskccjxx!getDataList.action' 
    
        score_html = self.session.post(get_score_url,headers=self.headers,\
                              
            cookies = requests.utils.dict_from_cookiejar(self.var_code.cookies),\
                              
            data=datas)


        # 把成绩保存为.txt文件,内容为json格式    
        with open( self.account+'.txt','wb') as f: 
        
             f.write(score_html.content)
        
             f.close()

        self.data_processing()

    # 本地文件的数据处理        
    def data_processing(self): 

    
        try :

            with open( self.account+'.txt','r',encoding = 'utf-8') as f:

                # 转换json格式为字典格式    
                data = json.load(f) 

                # 获取list格式的成绩
                datas = data['rows'] 

                totals = data['total'] 

                f.close()

            with open(self.account + '.txt','w',encoding = 'utf-8') as d:

                jd_sum = 0.0

                # 遍历list 获取科目、成绩和绩点    
                for i in  datas : 

                    jd_sum += float(i['cjjd'])
        
                    scores =  i['kcmc'] + ' : ' + i['zcj']+',   ' + '绩点' + ' : ' + i['cjjd'] + '\n' +'\n'

                    # 此为验证成绩是否正确，可注释掉                    
                    print (i['kcmc'] + ' : ' + i['zcj'])   

                    d.write(scores)

                 # 平均绩点
                jd_ave =  '平均绩点:   ' +  str(jd_sum / int(totals) )

                print (jd_ave)

                d.write(jd_ave)
                
                d.close()

        except :

            print('获取成绩失败！')

if __name__ == '__main__' :
    
    Crawler_score()
                






 
