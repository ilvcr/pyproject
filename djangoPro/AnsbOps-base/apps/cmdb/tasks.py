from __future__ import absolute_import, unicode_literals
import json
from multiprocessing import current_process
from apps.cmdb import  models as asset_db
from tools import get_os_info,ansible_api
from AnsbOps.celery import app
from AnsbOps.settings import BASE_DIR

@app.task
def sync_os_info():
    current_process()._config = {'semprefix': '/mp'}
    asset_obj = asset_db.Asset.objects.all()
    host_list = []
    for  i in asset_obj:
        ip = i.asset_ip
        host_list.append(ip)
    os_info = get_os_info.main(host_list)

    for i in os_info.keys():
        host_obj = asset_db.Asset.objects.get(asset_ip=i)
        data = os_info[i]
        os_obj = asset_db.AssetOsInfo.objects.get(asset_id=host_obj.id)
        os_obj.hostname=data['localhost']
        os_obj.os_type=data['kernel']
        os_obj.kernel_version="{} {}".format(data['kernel'], data['kernelrelease'])
        os_obj.os_version="{} {}".format(data['os'], data['osrelease'])
        os_obj.product_name=data['productname']
        os_obj.cpu_model=data['cpu_model']
        os_obj.cpu_core_count=data['num_cpus']
        os_obj.mem_size=data['mem_size']
        os_obj.save()

        asset_db.NIC.objects.filter(asset_id=host_obj.id).delete()
        for j in data['interface']:
            nic_obj = asset_db.NIC(asset_id=host_obj.id, name=j["label"], model=j["type"], mac=j["hwaddr"],
                                   ip_address=j["address"], net_mask=j["netmask"], mtu=j["mtu"])
            nic_obj.save()

        asset_db.Devices.objects.filter(asset_id=host_obj.id).delete()
        for k in data['devices_list']:
            device_obj = asset_db.Devices(asset_id=host_obj.id, device_name=k["device_name"],
                                          device_model=k["device_model"], device_size=k["device_size"],
                                          interface_type=k["interface_type"])
            device_obj.save()
        asset_db.Mounts.objects.filter(asset_id=host_obj.id).delete()
        for h in data['mount_list']:
            mount_obj = asset_db.Mounts(asset_id=host_obj.id, device=h["device"],
                                        mount=h["mount"], size_total=h["size_total"], size_available=h["size_available"],
                                        fstype=h["fstype"])
            mount_obj.save()

    module_name = 'script'

    module_args = "{}{}".format(BASE_DIR,"/tools/get_netstat_info.py")
    ret = ansible_api.run_ansible(module_name, module_args, host_list)
    data = json.loads(ret)
    server_info = data['success']
    for i in server_info.keys():
        host_obj = asset_db.Asset.objects.get(asset_ip=i)
        data = server_info[i]["stdout_lines"]
        asset_db.RunServer.objects.filter(asset_id=host_obj.id).delete()
        for j in json.loads(data[0]):
            server_obj = asset_db.RunServer(asset_id=host_obj.id, server_name=j[0], server_version=j[1],
                                            server_port=json.dumps(j[2]))
            server_obj.save()
    return "success"
