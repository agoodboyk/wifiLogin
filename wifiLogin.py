#coding:utf-8
#联通wifi登陆，
import requests ,sys ,re ,os ,socket ,time
reload(sys)
sys.setdefaultencoding('utf-8')
TIME_INTERVAL = 60 #检查网络畅通时间间隔
ACCOUNT = '13247710502' #wifi账号
PASSWORD = '618769' #wifi密码
def login():
    #s = requests.session()#后面需要session.close()
    url0 = 'http://www.baidu.com'
    r=requests.get(url0)
    IP = re.findall(r'=\d+\.\d+\.\d+\.\d+' , r.url)[0][1:]    
    url = 'http://220.248.195.1:8888/login.do'
    data = {
       'browserType': 'pc',
       'Country': 'Croatia',
       'CSRFToken_HW': '801a0a8b27b8df7dbfe71e2639655938',
       'domain': 'jx',
       'Operator': 'T-Mobile',
       'password': PASSWORD,
       'textPWD': '%E8%AF%B7%E8%BE%93%E5%85%A5WLAN%E6%9C%8D%E5%8A%A1%E5%AF%86%E7%A0%81',
       'userAgent': 'Mozilla%2F5.0+%28Windows+NT+10.0%3B+WOW64%3B+Trident%2F7.0%3B+rv%3A11.0%29+like+Gecko+Core%2F1.53.3427.400+QQBrowser%2F9.6.12513.400',
       'username': ACCOUNT,
       'wlanacname': '',
       'wlanuserip': IP
       }
    r = requests.post(url,data=data)
    print time.strftime('%X',time.localtime()) + ' : 连接成功'
    return True
def keep_alive():
    while True:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(('httpbin.org',80))
    #sock = socket.ssl(sock)
        req = 'GET /ip HTTP/1.1\r\n\
Host:httpbin.org\r\n\r\n'
        sock.send(req)
        results = sock.recv(1024)
        #print(results)
        if 'origin' in results:
            sock.close()
            print time.strftime('%X',time.localtime()) + ' : ok'
        else:
            print time.strftime('%X',time.localtime()) + ' : 正在重新登录……'
            sock.close()
            login()
        time.sleep(TIME_INTERVAL)
        continue
if __name__ == '__main__':
    keep_alive()

