#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('AK', 'SK', 'default')) #替换为所需的 AK 和 SK

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')#替换为服务所在地址
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('PhoneNumbers', "13820000000")#替换为所要发送的手机号
request.add_query_param('SignName', "你的签名")#替换为所需的签名
request.add_query_param('TemplateCode', "SMS_XXXXX")#替换为所需的模板
request.add_query_param('TemplateParam', "{\"content\":\" 这是测试信息\"}")

response = client.do_action(request)
# python2:  print(response) 
print(str(response, encoding = 'utf-8'))
