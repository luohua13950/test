# -*- coding: utf-8 -*-
__author__ = 'luohua139'
import yaml
import sys
from djtwo.settings import BASE_DIR
sys.path.append('../../')
url = '../../conf/'
def read_yaml_file(file_name):
    ret = yaml.load(file(file_name))
    ret_ip = ret['hosts']['ipadress']
    #print ret_ip[0],len(ret_ip)
    return ret
if __name__ == '__main__':
        file_name = 'hosts.yaml'
        ret = read_yaml_file(file_name)