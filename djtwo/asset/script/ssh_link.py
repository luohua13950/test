# -*- coding: utf-8 -*-
__author__ = 'luohua139'
import paramiko
import re
HostIp = '180.76.159.87'
port = 22
username = 'root'
password = 'luohua139@'
def ssh_login_basetion():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HostIp,port,username,password)
    except Exception as e:
        print HostIp+"is can't connection"
    return ssh

def get_memory(ssh):
        stdin,stdout,stderr=ssh.exec_command('free -m |awk \' NR==2 {print $3" "$4" "$7}\'')
        res_err = stderr.readlines()
        if len(res_err) !=0:
            return False;
        else:
            res_out = stdout.readlines()
        out_context =  res_out
        #ssh.close()
        try:
            if len(out_context) != 0:
                #去除/n 等
                res = out_context[0].strip()
                #Unicode转换为ASCII string类型
                str_res = res.encode("ascii")
                #转为字符串数组
                ret = str_res.split()
                return ret
            else:
                res = "无法获取"

                return res
        except Exception as e:
            ret = "无法得到内存信息，请检查"
            return ret

def get_cpu_info(ssh):
    stdin,stdout,stderr =ssh.exec_command('sar 2 3 |awk \'END {print 100-$NF}\'')
    #stdin,stdout,stderr =ssh.exec_command('sar 2 3 |awk \'END {print NR=$3,$5,$8}\'')
    res_err = stderr.readlines()
    if len(res_err) != 0:
        print "获取CPU信息时发生错误"
        return False
    else:
        out = stdout.readlines()
    out_context = out[0].strip()
    try:
        if len(out_context) != 0:
            res_out = round(float(out_context),2)
            #print res_out
            return res_out
    except Exception as e:
        ret = "无法查询到CPU信息"
        print ret

def get_space(ssh):
    stdin,stdout,stderr = ssh.exec_command('df -h |awk \' NR>1 {if ($1==$NF){print $1}else{print $0}}\'')
    res_err = stderr.readlines()
    if len(res_err) != 0:
        print "获取磁盘空间失败"
        return False
    else:
        out = stdout.readlines()
    res_out = out
    try:
        if len(res_out) != 0:
            res =' '.join(res_out)
            str_res = res.encode("ascii")
            percent = re.findall(r'\d{1,2}%',str_res)
            #exclude_per = re.findall(r'\s+\d+([.]{1}[0-9]+){0,1}\w',str_res)
            print str_res,percent
            return percent
        else:
            print "获取输出时出现异常"
    except Exception as e:
        print (e)

if __name__ == '__main__':
    ss = ssh_login_basetion()
    #tt = get_memory(ss)
   # cc = get_cpu_info(ss)
    bb = get_space(ss)
    ss.close()
