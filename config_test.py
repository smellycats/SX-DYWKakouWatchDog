#-*- encoding: utf-8 -*-
from ini_conf import MyIni


class ConfigTest(object):
    def __init__(self):
        self.my_ini = MyIni()
        
    def test_kakou(self):
        print self.my_ini.get_kakou()

    def test_sms(self):
        print self.my_ini.get_sms()

    def test_mobiles(self):
        print self.my_ini.get_mobiles()['number'].split(',')


if __name__ == "__main__":
    ct = ConfigTest()
    ct.test_kakou()
    ct.test_sms()
    ct.test_mobiles()
