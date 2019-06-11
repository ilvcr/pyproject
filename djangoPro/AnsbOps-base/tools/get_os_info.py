# -*- coding: utf-8 -*-

# @Time    : 2019-01-15 10:55
# @Author  : 小贰
# @FileName: get_sofeware.py
# @function: 通过ansible setup 模块获取服务器基础信息

import json
from tools import ansible_api



def main(host_list, ansible_user="root"):
    """
    :param host_list:['127.0.0.1']
    :param option_dict:{"become": True, "remote_user": "opadmin"}
    """
    module_name = 'setup'
    module_args = ""
    result = ansible_api.run_ansible(module_name, module_args, host_list,ansible_user)
    result = json.loads(result)['success']
    data = {}
    for i in result.keys():
        info = result[i]['ansible_facts']
        hostname = info['ansible_hostname']
        kernel = info['ansible_system']
        kernelrelease = info['ansible_kernel']
        cpu_model = info['ansible_processor'][2]
        num_cpus = info['ansible_processor_cores']
        productname = info['ansible_product_name']
        os_name = info['ansible_distribution']
        osrelease = info['ansible_distribution_version']
        mem_info = info['ansible_memory_mb']
        disk_info = info['ansible_devices']
        mount_info = info['ansible_mounts']
        interfaces = info['ansible_interfaces']
        inter_list = []
        devices_list = []
        mount_list = []
        #磁盘信息
        for k in disk_info.keys():
            devices_list.append({"device_name":'/dev/{}'.format(k),"device_size":disk_info[k]['size'],"device_model":disk_info[k]['model'],"interface_type":disk_info[k]["host"]})

        for h in mount_info:
            mount_list.append({"size_total": h['size_total'], "size_available": h['size_available'], "device": h['device'], "mount": h["mount"], "fstype": h["fstype"]})

        #网卡信息
        for j in interfaces:
            try:
                key = "ansible_%s" % j
                inter_ipv4 = info[key]['ipv4']
                inter_ipv4["label"] = j
                try:
                    inter_ipv4["hwaddr"] = info[key]['macaddress']
                except:
                    inter_ipv4["hwaddr"] = "00:00:00:00:00:00"
                inter_ipv4["mtu"] = info[key]['mtu']
                inter_ipv4["type"]= info[key]['type']
                inter_list.append(inter_ipv4)
            except:
                continue

        new_info={"localhost": hostname,"kernel":kernel,"kernelrelease": kernelrelease,
                "cpu_model":cpu_model,"num_cpus": num_cpus,"productname":productname,
                "os": os_name,"osrelease":osrelease ,"mem_size":mem_info["real"]['total'],"interface": inter_list,"devices_list":devices_list,"mount_list":mount_list}
        data[i] = new_info
    return data

if __name__ == "__main__":
    ansible_user = "root"
    host_list = ["192.168.145.128","192.168.145.129"]
    result = main(host_list, ansible_user)
    print(json.dumps(result,indent=4))


