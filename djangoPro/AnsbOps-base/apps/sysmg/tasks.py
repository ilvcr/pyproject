from __future__ import absolute_import, unicode_literals
from AnsbOps.celery import app
import json
from tools import ansible_api
from multiprocessing import current_process

@app.task
def install_server(ip_list,script_file):
    current_process()._config = {'semprefix': '/mp'}
    host_list = json.loads(ip_list)
    ansible_user="root"
    module_name = 'script'
    module_args = script_file
    ret = ansible_api.run_ansible(module_name,module_args,host_list,ansible_user)
    return ret



