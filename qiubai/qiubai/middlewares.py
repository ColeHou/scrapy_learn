#-*- coding=utf-8 -*-
import random

agents = [
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',

]



class RandomChoiceUserAgent(object):
    def process_request(self,request,spider):
        request.headers["User-Agent"] = random.choice(agents)

class PrintUserAgent(object):
    def process_request(self,request,spider):
        print (request.headers["User-Agent"])
