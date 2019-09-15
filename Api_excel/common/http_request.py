#coding=utf-8

import requests
from Api_excel.common.config import config

class HttpRequest:

    def request(self,url,method,data=None,json=None,cookies=None):

        method = method.upper()  # 将method强制转成全大小
        # url 配置地址+excel请求地址
        url=config.get("api","pre_url")+url

        if type(data) == str:
            data = eval(data)  # str转成字典

        if method == 'GET':
            resp = requests.get(url, params=data, cookies=cookies)  # resp 是Response对象
        elif method == 'POST':
            if json:
                resp = requests.post(url, json=json, cookies=cookies)
            else:
                resp = requests.post(url, data=data, cookies=cookies)
        else:
            resp = None
            print('UN-support method')

        return resp
class HttpRequest_Session:
    def __init__(self):
        # 打开一个session 建立一个session
        self.session=requests.sessions.session()

    def request(self,method,url,data=None,json=None):
        # 强转大写
        method=method.upper()
        # url 配置地址+excel请求地址
        url = config.get("api", "pre_url") + url
        print('请求url:', url)
        print('请求data:', data)
        if type(data)==str:
            data=eval(data)
        if method=="GET":
            resp=self.session.request(method=method,url=url,params=data)
        elif method=="POST":
            if json:
                resp=self.session.request(method=method, url=url, json=json)
            else:
                resp=self.session.request(method=method, url=url, data=data)
        else:
            resp=None
            print("其他请求方法")

        print('请求response:', resp.text)
        return resp

    def close(self):
        self.session.close()


#
# if __name__ == '__main__':
#     data1 = {"mobilephone":"17796352123","pwd":"123456"}
#     http_request1=HttpRequest().request("http://test.lemonban.com/futureloan/mvc/api/member/login","POST",data1)

    # data2={"mobilephone":"17796352123","amount":"200"}
    # http_request2=HttpRequest().request("http://test.lemonban.com/futureloan/mvc/api/member/recharge","POST",data2,cookies=http_request1.cookies)

    # print(http_request1.text)
    # print(http_request1.cookies)
    # print(http_request1.request._cookies)

    # print(http_request2.text)
    # print("-------------------分界线---------------------")
    #
    # http_request_session=HttpRequest_Session()
    # resp=http_request_session.request("POST","http://test.lemonban.com/futureloan/mvc/api/member/login",data1)
    # resp=http_request_session.request("POST","http://test.lemonban.com/futureloan/mvc/api/member/recharge",data2)
    # resp.close()
    #
    # print(resp.text)
    # print(resp.cookies)
    # print(resp.request._cookies)