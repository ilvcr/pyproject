from django.db.models import Q
from apps.rbac import models as rbac_db

def menus_list(username=None,role_id=None):
    '''获取菜单列表'''
    if username:
        user_obj = rbac_db.User.objects.get(Q(user=username) | Q(email=username)| Q(phone=username))
        role_id=user_obj.role_id
    else:
        role_id = role_id
    role_obj = rbac_db.Role.objects.get(id=role_id)
    data_list = []
    if role_obj.role == "admin":
        one_menu = rbac_db.Permssions.objects.filter(perms_type__contains="一级菜单")
        for i in one_menu:
            two_menu = rbac_db.Permssions.objects.filter(parent_id=i.id)
            two_menu_list = []
            for j in two_menu:
                two_menu_list.append({"id":j.id,'perms': j.perms, 'perms_url': j.perms_url, 'perms_img': j.perms_img})
            data_list.append({"id":i.id,'perms': i.perms, 'perms_url': i.perms_url, 'perms_img': i.perms_img,"two_menu":two_menu_list})
    else:
        perms_obj = role_obj.perms.all()
        one_menu_list = []
        for i  in perms_obj:
            perms_type = i.perms_type
            if perms_type == u'一级菜单':
                one_menu_list.append({"id":i.id,'perms': i.perms, 'perms_url': i.perms_url, 'perms_img': i.perms_img,"perms_id":i.id})
        for i in one_menu_list:
            two_menu_list = []
            for j in perms_obj:
                if j.parent_id == i["perms_id"]:
                    two_menu_list.append({"id":j.id,'perms': j.perms, 'perms_url': j.perms_url, 'perms_img': j.perms_img})
            i["two_menu"] = two_menu_list
            data_list.append(i)
    return data_list


def perms_list(username):
    user_obj = rbac_db.User.objects.get(Q(user=username) | Q(email=username) | Q(phone=username))
    role_id = user_obj.role_id
    role_obj = rbac_db.Role.objects.get(id=role_id)
    perms_all_list = []
    if role_obj.role == "admin":
        perms_obj = rbac_db.Permssions.objects.all()
        for i in perms_obj:
            perms_all_list.append(i.perms_id)
    else:
        perms_obj = role_obj.perms.all()
        for i in perms_obj:
            perms_all_list.append(i.perms_id)
    return perms_all_list

def perms_id_list(role_id):
    role_obj = rbac_db.Role.objects.get(id=role_id)
    perms_all_list = []
    if role_obj.role == "admin":
        perms_obj = rbac_db.Permssions.objects.all()
        for i in perms_obj:
            perms_all_list.append(i.id)
    else:
        perms_obj = role_obj.perms.all()
        for i in perms_obj:
            perms_all_list.append(i.id)
    return perms_all_list