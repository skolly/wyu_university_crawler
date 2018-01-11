# wyu_university_crawler
五邑大学新子系统爬虫（python）

主要思路：
  
  1、获取验证码，处理验证码（自动识别验证码尚未完成）。
    #verify_url = 'http://202.192.240.29/yzm?d=1512785249083'
  
 2、输入学号和密码，处理数据。
    #
    学号 = account    
    密码 = pwd    
    验证码 = vercode  
    
  3、模仿浏览器发送数据给接收数据的网址,登录子系统。
    #login_url = 'http://202.192.240.29/new/login'
  
  4、获取成绩并处理数据。
    #get_score_url = 'http://202.192.240.29/xskccjxx!getDataList.action'

