# -*- coding: utf-8 -*-
import json

import requests
from requests.auth import HTTPBasicAuth


class SMS(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.user = kwargs['user']
	self.pwd = kwargs['pwd']
        self.headers = {'content-type': 'application/json'}

    def sms_send(self, content, mobiles):
        """发送短信"""
        url = 'http://{host}:{port}/sms'.format(host=self.host, port=self.port)
        data = {'content': content, 'mobiles': mobiles}
        try:
            r = requests.post(
                url, headers=self.headers, data=json.dumps(data),
		auth=HTTPBasicAuth(self.user, self.pwd))
            if r.status_code == 201:
                return json.loads(r.text)
        except Exception as e:
            print 'sms:',e

