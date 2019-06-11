import os
import re
import commands

ret = os.popen("netstat -tnlp | grep tcp|awk '{print $4,$7}'")
port_pid_list = []
pid_list = []
for  i in ret.readlines():
    port,pid = i.strip(":\n").split(":")[-1].split("/")[0].split()
    pid_list.append(pid)
    port_pid_list.append({pid:port})

new_pid_list = list(set(pid_list))
port_pid_dict = {}
for i in new_pid_list:
    port_list = []
    for j in port_pid_list:
        try:
            port_list.append(j[i])
        except:
            continue
    port_list = list(set(port_list))
    port_pid_dict[i]=port_list

server_info = []

for i in port_pid_dict.keys():
    ps_cmd = "ps aux | grep -v grep | grep {}".format(i)
    ret = os.popen(ps_cmd)
    server_name = ret.read().strip("\n").split()[10].rstrip(":")
    if server_name == "php-fpm":
        server_name = "php"
    if re.search("erlang",server_name):
         server_info.append([server_name,"otp_src_20.3",port_pid_dict[i]])
    else:
        version_cmd = "{} --version||{} -V".format(server_name,server_name)
        ret = commands.getoutput(version_cmd)
        version_info = re.search("\d+\.\d+", ret)
        if version_info:
            server_info.append([server_name,version_info.group(),port_pid_dict[i]])
        else:
            server_info.append([server_name,"Unkonwn",port_pid_dict[i]])


print(server_info)
