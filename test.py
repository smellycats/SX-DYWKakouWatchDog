# -*- coding: utf-8 -*-
from helper_sms import SMS
from helper_kakou import Kakou

kakou_ini = {'host': '10.47.187.123', 'port': 80}
sms_ini = {'host': '10.47.187.123', 'port': 8090}

def get_kkdd_test():
    kk = Kakou(**kakou_ini)
    print kk.get_kkdd('441302')
    print kk.get_kkdd('441304')

def get_kakou_count_test():
    kk = Kakou(**kakou_ini)
    print kk.get_kakou_count(st='2016-02-29 11:23:45',
                             et='2016-02-29 14:23:45',
                             kkdd='441302001', fxbh='IN')

def check_kakou_count_test():
    kk = Kakou(**kakou_ini)
    kkdd_list = []
    for i in ['441302', '441304']:
        kkdd_list += kk.get_kkdd(i)
    for i in kkdd_list:
        for fx in i['fxbh_list']:
            count = kk.get_kakou_count(
                        st='2016-02-29 11:23:45',
                        et='2016-02-29 14:23:45',
                        kkdd=i['kkdd_id'], fxbh=fx)
            print u'{0}{1}:{2}'.format(i['kkdd_name'], fx, count)

def sms_test():
    sms = SMS(**sms_ini)
    sms.sms_send(u'死肥子', ['15819851862'])

if __name__ == '__main__':
    #get_kkdd_test()
    #get_kakou_count_test()
    #check_kakou_count_test()
    sms_test()
