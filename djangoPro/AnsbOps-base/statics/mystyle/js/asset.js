///////////////////////资产/////////////////////////////
//添加资产
$("#sub-asset").click(function(){
    var asset_ip = $("#asset-ip").val();
    var login_port = $("#login-port").val();
    var login_user = $("#login-user").val();
    var login_passwd = $("#login-passwd").val();
    var login_method = $("#login-method").val();
    var asset_type = $("#asset-type").val();
    var asset_model = $("#asset-model").val();
    var asset_group = $("#asset-group").val();
    var asset_idc = $("#asset-idc").val();
    var asset_changshang = $("#asset-changshang").val();
    var asset_msg = $("#asset-msg").val();
    var asset_sn = $("#asset-sn").val();
    var purchase_time = $("#purchase-time").val();
    var expire_time = $("#expire-time").val();
    $.ajax({
        url: "/cmdb/asset/",
        type: 'POST',
        data: {
            'asset_ip': asset_ip,
            'login_port': login_port,
            "login_user": login_user,
            "login_passwd": login_passwd,
            "login_method": login_method,
            "asset_type":asset_type,
            "asset_model":asset_model,
            "asset_group":asset_group,
            "asset_idc":asset_idc,
            "asset_changshang":asset_changshang,
            "asset_msg":asset_msg,
            "asset_sn":asset_sn,
            "purchase_time":purchase_time,
            "expire_time":expire_time,
        },
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template:ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                $("#assetModal").modal("hide");
                spop({
                    template: ret.info,
                    style: 'success',
                    autoclose: 3000
                });
                setTimeout("location.reload()",3000);
            }
        }
    })
});

//获取编辑IDC信息
$('td a[name="edit-asset"]').click(function() {
    var asset_id = $(this).attr("asset_id");
    $.ajax({
        url: "/cmdb/asset/",
        type: "PUT",
        data: JSON.stringify({'asset_id': asset_id}),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template: ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                if (ret.status =="True"){
                    info = ret.info;
                    $("#edit-asset-ip").val(info.asset_ip);
                    $("#edit-login-port").val(info.login_port);
                    $("#edit-login-user").val(info.login_user);
                    $("#edit-login-passwd").val(info.login_passwd);
                    $("#edit-login-method").val(info.login_method);
                    $("#edit-asset-type").val(info.asset_type);
                    $("#edit-asset-model").val(info.asset_model);
                    $("#edit-asset-group").val(info.asset_group);
                    $("#edit-asset-idc").val(info.asset_idc);
                    $("#edit-asset-changshang").val(info.asset_changshang);
                    $("#edit-asset-msg").val(info.asset_msg);
                    $("#edit-asset-sn").val(info.asset_sn);
                    $("#edit-purchase-time").val(info.purchase_time);
                    $("#edit-expire-time").val(info.expire_time);
                    $("#sub-edit-asset").attr('asset_id',info.asset_id);
                    $("#edit-assetModal").modal('show');
                }else {
                    spop({
                        template: ret.info,
                        autoclose: 3000
                    });
                }
            }
        }
    });
});

//修改资产信息
$("#sub-edit-asset").click(function() {
    var asset_id = $(this).attr("asset_id");
    var asset_ip = $("#edit-asset-ip").val();
    var login_port = $("#edit-login-port").val();
    var login_user = $("#edit-login-user").val();
    var login_passwd = $("#edit-login-passwd").val();
    var login_method = $("#edit-login-method").val();
    var asset_type = $("#edit-asset-type").val();
    var asset_model = $("#edit-asset-model").val();
    var asset_group = $("#edit-asset-group").val();
    var asset_idc = $("#edit-asset-idc").val();
    var asset_changshang = $("#edit-asset-changshang").val();
    var asset_msg = $("#edit-asset-msg").val();
    var asset_sn = $("#edit-asset-sn").val();
    var purchase_time = $("#edit-purchase-time").val();
    var expire_time = $("#edit-expire-time").val();
    $.ajax({
        url: "/cmdb/asset/",
        type: "PUT",
        data: JSON.stringify({
            'action':'edit',
            'asset_id': asset_id,
            'asset_ip': asset_ip,
            'login_port': login_port,
            "login_user": login_user,
            "login_passwd": login_passwd,
            "login_method": login_method,
            "asset_type":asset_type,
            "asset_model":asset_model,
            "asset_group":asset_group,
            "asset_idc":asset_idc,
            "asset_changshang":asset_changshang,
            "asset_msg":asset_msg,
            "asset_sn":asset_sn,
            "purchase_time":purchase_time,
            "expire_time":expire_time,
        }),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
            }else {
                $("#edit-assetModal").modal("hide");
                spop({
                    template: ret.info,
                    style: 'success',
                    autoclose: 3000
                });
                setTimeout("location.reload()",3000);
            }
        }
    });
});

//删除资产
$("td a[name='del-asset']").click(function(){
    var asset_id = $(this).attr('asset_id');
    var statu = confirm("是否确认删除！");
    if (statu==true)
    {
        $.ajax({
            url: "/cmdb/asset/",
            type: "DELETE",
            data: JSON.stringify({'asset_id':asset_id}),
            success: function(data) {
                var ret = eval('(' + data + ')');
                if(ret.status =="perms_false"){
                    spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
                }else {
                    spop({
                        template: ret.info,
                        style: 'success',
                        autoclose: 3000
                    });
                    setTimeout("location.reload()",3000);
                }
             }
        });
    }
});



///////////////////////机房/////////////////////////////
//添加机房
$("#sub-idc").click(function(){
    var idc_name = $("#idc-name").val();
    var idc_msg = $("#idc-msg").val();
    var contact = $("#contact").val();
    var contact_phone = $("#contact-phone").val();
    var contact_email = $("#contact-email").val();
    $.ajax({
        url: "/cmdb/idc/",
        type: 'POST',
        data: {
            'idc_name': idc_name,
            'idc_msg': idc_msg,
            "contact": contact,
            "contact_phone": contact_phone,
            "contact_email": contact_email,
        },
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template:ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                $("#idcModal").modal("hide");
                spop({
                    template: ret.info,
                    style: 'success',
                    autoclose: 3000
                });
                setTimeout("location.reload()",3000);
            }
        }
    })
});

//获取编辑IDC信息
$('td a[name="edit-idc"]').click(function() {
    var idc_id = $(this).attr("idc_id");
    $.ajax({
        url: "/cmdb/idc/",
        type: "PUT",
        data: JSON.stringify({'idc_id': idc_id}),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template: ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                if (ret.status =="True"){
                    info = ret.info;
                    $("#edit-idc-name").val(info.idc_name);
                    $("#edit-idc-msg").val(info.idc_msg);
                    $("#edit-contact").val(info.contact);
                    $("#edit-contact-phone").val(info.contact_phone);
                    $("#edit-contact-email").val(info.contact_email);
                    $("#sub-edit-idc").attr('idc_id',info.idc_id);
                    $("#edit-idcModal").modal('show');
                }else {
                    spop({
                        template: ret.info,
                        autoclose: 3000
                    });
                }

            }

        }
    });
});

//修改idc信息
$("#sub-edit-idc").click(function() {
    var idc_id = $(this).attr("idc_id");
    var idc_name = $("#edit-idc-name").val();
    var idc_msg = $("#edit-idc-msg").val();
    var contact = $("#edit-contact").val();
    var contact_phone = $("#edit-contact-phone").val();
    var contact_email = $("#edit-contact-email").val();
    $.ajax({
        url: "/cmdb/idc/",
        type: "PUT",
        data: JSON.stringify({'action':'edit','idc_id':idc_id,'idc_name':idc_name,
            'idc_msg':idc_msg,'contact':contact, 'contact_phone':contact_phone,
            'contact_email':contact_email}),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
            }else {
                $("#edit-idcModal").modal("hide");
                spop({
                    template: ret.info,
                    style: 'success',
                    autoclose: 3000
                });
                setTimeout("location.reload()",3000);
            }
        }
    });
});

//删除IDC
$("td a[name='del-idc']").click(function(){
    var idc_id = $(this).attr('idc_id');
    var statu = confirm("是否确认删除！");
    if (statu==true)
    {
        $.ajax({
            url: "/cmdb/idc/",
            type: "DELETE",
            data: JSON.stringify({'idc_id':idc_id}),
            success: function(data) {
                var ret = eval('(' + data + ')');
                if(ret.status =="perms_false"){
                    spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
                }else {
                    spop({
                        template: ret.info,
                        style: 'success',
                        autoclose: 3000
                    });
                    setTimeout("location.reload()",3000);
                }
             }
        });
    }
});

///////////////////////厂商/////////////////////////////

//添加厂商
$("#sub-changshang").click(function(){
    var changshang = $("#changshang").val();
    var contact = $("#contact").val();
    var contact_phone = $("#contact-phone").val();
    var contact_email = $("#contact-email").val();
    $.ajax({
        url: "/cmdb/changshang/",
        type: 'POST',
        data: {
            'changshang': changshang,
            "contact": contact,
            "contact_phone": contact_phone,
            "contact_email": contact_email,
        },
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template:ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                $("#changshangModal").modal("hide");
                spop({
                    template: ret.info,
                    style: 'success',
                    autoclose: 3000
                });
                setTimeout("location.reload()",3000);
            }
        }
    })
});

//获取编辑changshang信息
$('td a[name="edit-changshang"]').click(function() {
    var changshang_id = $(this).attr("changshang_id");
    $.ajax({
        url: "/cmdb/changshang/",
        type: "PUT",
        data: JSON.stringify({'changshang_id': changshang_id}),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template: ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                if (ret.status =="True"){
                    info = ret.info;
                    $("#edit-changshang").val(info.changshang);
                    $("#edit-contact").val(info.contact);
                    $("#edit-contact-phone").val(info.contact_phone);
                    $("#edit-contact-email").val(info.contact_email);
                    $("#sub-edit-changshang").attr('changshang_id',info.changshang_id);
                    $("#edit-changshangModal").modal('show');
                }else {
                    spop({
                        template: ret.info,
                        autoclose: 3000
                    });
                }

            }

        }
    });
});

//修改changshang信息
$("#sub-edit-changshang").click(function() {
    var changshang_id = $(this).attr("changshang_id");
    var changshang = $("#edit-changshang").val();
    var contact = $("#edit-contact").val();
    var contact_phone = $("#edit-contact-phone").val();
    var contact_email = $("#edit-contact-email").val();
    $.ajax({
        url: "/cmdb/changshang/",
        type: "PUT",
        data: JSON.stringify({'action':'edit','changshang_id':changshang_id,'changshang':changshang,
            'contact':contact, 'contact_phone':contact_phone, 'contact_email':contact_email}),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
            }else {
                $("#edit-changshangModal").modal("hide");
                spop({
                    template: ret.info,
                    style: 'success',
                    autoclose: 3000
                });
                setTimeout("location.reload()",3000);
            }
        }
    });
});

//删除changshang
$("td a[name='del-changshang']").click(function(){
    var changshang_id = $(this).attr('changshang_id');
    var statu = confirm("是否确认删除！");
    if (statu==true)
    {
        $.ajax({
            url: "/cmdb/changshang/",
            type: "DELETE",
            data: JSON.stringify({'changshang_id':changshang_id}),
            success: function(data) {
                var ret = eval('(' + data + ')');
                if(ret.status =="perms_false"){
                    spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
                }else {
                    spop({
                        template: ret.info,
                        style: 'success',
                        autoclose: 3000
                    });
                    setTimeout("location.reload()",3000);
                }
             }
        });
    }
});

///////////////////////分组/////////////////////////////
//添加分组
$("#sub-group").click(function(){
    var group_name = $("#group-name").val();
    var group_msg = $("#group-msg").val();
    var user_id = $("#contact").val();
    $.ajax({
        url: "/cmdb/group/",
        type: 'POST',
        data: {
            'group_name': group_name,
            'group_msg': group_msg,
            "user_id": user_id,
        },
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template:ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                $("#groupModal").modal("hide");
                spop({
                    template: ret.info,
                    style: 'success',
                    autoclose: 3000
                });
                setTimeout("location.reload()",3000);
            }
        }
    })
});

//获取编辑group信息
$('td a[name="edit-group"]').click(function() {
    var group_id = $(this).attr("group_id");
    $.ajax({
        url: "/cmdb/group/",
        type: "PUT",
        data: JSON.stringify({'group_id': group_id}),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template: ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                if (ret.status =="True"){
                    info = ret.info;
                    $("#edit-group-name").val(info.group_name);
                    $("#edit-group-msg").val(info.group_msg);
                    $("#edit-contact").val(info.user_id);
                    $("#sub-edit-group").attr('group_id',info.group_id);
                    $("#edit-groupModal").modal('show');
                }else {
                    spop({
                        template: ret.info,
                        autoclose: 3000
                    });
                }

            }

        }
    });
});

//修改group信息
$("#sub-edit-group").click(function() {
    var group_id = $(this).attr("group_id");
    var group_name = $("#edit-group-name").val();
    var group_msg = $("#edit-group-msg").val();
    var user_id = $("#edit-contact").val();
    $.ajax({
        url: "/cmdb/group/",
        type: "PUT",
        data: JSON.stringify({'action':'edit','group_id':group_id,'group_name':group_name,
            'group_msg':group_msg,'user_id':user_id}),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
            }else {
                $("#edit-groupModal").modal("hide");
                spop({
                    template: ret.info,
                    style: 'success',
                    autoclose: 3000
                });
                setTimeout("location.reload()",3000);
            }
        }
    });
});

//删除group
$("td a[name='del-group']").click(function(){
    var group_id = $(this).attr('group_id');
    var statu = confirm("是否确认删除！");
    if (statu==true)
    {
        $.ajax({
            url: "/cmdb/group/",
            type: "DELETE",
            data: JSON.stringify({'group_id':group_id}),
            success: function(data) {
                var ret = eval('(' + data + ')');
                if(ret.status =="perms_false"){
                    spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
                }else {
                    spop({
                        template: ret.info,
                        style: 'success',
                        autoclose: 3000
                    });
                    setTimeout("location.reload()",3000);
                }
             }
        });
    }
});