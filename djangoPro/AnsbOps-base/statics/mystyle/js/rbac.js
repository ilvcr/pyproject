////////////////////////角色管理////////////////////////////
///添加角色
$("#sub-role").click(function(){
    var role = $("#role").val();
    var role_msg = $("#role-msg").val();
    $.ajax(
        {
        url:"/rbac/role/",
        type: 'POST',
        data:{'role':role, 'role_msg':role_msg},
        success:function(data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                    template: ret.info,
                    style: 'warning',
                    autoclose: 3000
                });
            }else {
                $("#roleModal").modal("hide");
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


//获取修改角色信息
$('td a[name="edit-role"]').click(function(){
    var role_id = $(this).attr("role_id");
    $.ajax({
        url: "/rbac/role/",
        type: "PUT",
        data: JSON.stringify({'role_id':role_id}),
        success: function(data) {
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
                    $("#edit-role").val(info.role);
                    $("#edit-role-msg").val(info.role_msg);
                    $("#sub-edit-role").attr('role_id', info.role_id);
                    $("#edit-roleModal").modal('show');
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

//修改角色信息
$("#sub-edit-role").click(function(){
    var role_id = $(this).attr('role_id');
    var role = $("#edit-role").val();
    var role_msg = $("#edit-role-msg").val();
    $.ajax({
        url: "/rbac/role/",
        type: "PUT",
        data: JSON.stringify({'action':'edit','role':role, 'role_msg':role_msg,'role_id':role_id}),
        success: function(data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
            }else {
                $("#edit-roleModal").modal("hide");
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

//删除角色
$("td a[name='del-role']").click(function(){
   var role_id = $(this).attr('role_id');
   var statu = confirm("是否确认删除！");
   if (statu==true)
    {
        $.ajax({
            url: "/rbac/role/",
            type: "DELETE",
            data: JSON.stringify({'role_id':role_id}),
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

////////////////////////用户管理////////////////////////////

//添加用户
$("#add-user").click(function(){
    var user = $("#user").val();
    var name = $("#name").val();
    var passwd = $("#passwd").val();
    var repasswd = $("#repasswd").val();
    var role_id = $("#role-id").val();
    var phone = $("#phone").val();
    var email = $("#email").val();
    if(passwd==repasswd){
        $.ajax({
            url:"/rbac/user/",
            type:"POST",
            data:{'user':user, 'name':name,'passwd':passwd,'role_id':role_id,'phone':phone,'email':email,"role_id":role_id},
            success:function(data){
                var ret = eval('(' + data + ')');
                if(ret.status =="perms_false"){
                    spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
                }else {
                    $("#userModal").modal("hide");
                    spop({
                        template: ret.info,
                        style: 'success',
                        autoclose: 3000
                    });
                    setTimeout("location.reload()",3000);
                }
            }
        })
    }else{
        spop({
            template: "两次输入密码不一致",
            style: 'error',
            autoclose: 3000
        });
    }
});

//获取用户修改信息
$('td a[name="edit-user"]').click(function(){
    var user_id = $(this).attr("user_id");
        $.ajax({
            url: "/rbac/user/",
            type: "PUT",
            data: JSON.stringify({'user_id':user_id}),
            success: function(data) {
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
                        $("#edit-name").val(info.name);
                        $("#edit-user").val(info.user);
                        $("#edit-repasswd").val(info.passwd);
                        $("#edit-phone").val(info.phone);
                        $("#edit-email").val(info.email);
                        $("#edit-role-id").val(info.role_id);
                        $("#sub-edit-user").attr('user_id', info.user_id);
                        $("#edit-userModal").modal('show');
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


//修改用户信息
$("#sub-edit-user").click(function(){
    var user_id = $(this).attr('user_id');
    var name = $("#edit-name").val();
    var user = $("#edit-user").val();
    var role_id = $("#edit-role-id").val();
    var phone = $("#edit-phone").val();
    var email = $("#edit-email").val();
     $.ajax({
        url: "/rbac/user/",
        type: "PUT",
        data: JSON.stringify({'action':'edit','name':name, 'user':user,'role_id':role_id,'phone':phone,'email':email,'user_id':user_id}),
        success: function(data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
            }else {
                $("#edit-userModal").modal("hide");
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

//删除用户
$("td a[name='del-user']").click(function(){
    var user_id = $(this).attr('user_id');
   var statu = confirm("是否确认删除！");
   if (statu==true)
    {
        $.ajax({
            url: "/rbac/user/",
            type: "DELETE",
            data: JSON.stringify({'user_id':user_id}),
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

////////////////////////权限管理////////////////////////////

//添加权限
$("#sub-perms").click(function(){
    var perms = $("#perms").val();
    var perms_img = $("#perms-img").val();
    var perms_method = $("#perms-method").val();
    var perms_type = $("#perms-type").val();
    var perms_parent = $("#perms-parent").val();
    var perms_url = $("#perms-url").val();
    $.ajax({
            url:"/rbac/perms/",
            type:"POST",
            data:{"perms":perms,"perms_type":perms_type,"perms_img":perms_img, "perms_parent":perms_parent,'perms_url':perms_url,"perms_method":perms_method},
            success:function(data){
                var ret = eval('(' + data + ')');
                if(ret.status =="perms_false"){
                    spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
                }else {
                    $("#permsModal").modal("hide");
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


//获取编辑权限信息
$('td a[name="edit-perms"]').click(function() {
    var perms_id = $(this).attr("perms_id");
    $.ajax({
        url: "/rbac/perms/",
        type: "PUT",
        data: JSON.stringify({'perms_id': perms_id}),
        success: function (data) {
            var ret = eval('(' + data + ')');
                if(ret.status =="perms_false"){
                    spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
                }else {
                    if (ret.status == "True") {
                        info = ret.info;
                        $("#edit-perms").val(info.perms);
                        $("#edit-perms-type").val(info.perms_type);
                        $("#edit-perms-url").val(info.perms_url);
                        $("#edit-perms-parent").val(info.perms_parent);
                        $("#edit-perms-method").val(info.perms_method);
                        $("#edit-perms-img").val(info.perms_img);
                        $("#sub-edit-perms").attr('perms_id', info.perms_id);
                        $("#edit-permsModal").modal('show');
                    } else {
                        spop({
                            template: ret.info,
                            autoclose: 3000
                        });
                    }
                }
        }
    });
});

//修改权限信息
$("#sub-edit-perms").click(function() {
    var perms_id = $(this).attr("perms_id");
    var perms = $("#edit-perms").val();
    var perms_img = $("#edit-perms-img").val();
    var perms_method = $("#edit-perms-method").val();
    var perms_type = $("#edit-perms-type").val();
    var perms_parent = $("#edit-perms-parent").val();
    var perms_url = $("#edit-perms-url").val();
    $.ajax({
        url: "/rbac/perms/",
        type: "PUT",
        data: JSON.stringify({'action':'edit','perms_id':perms_id,'perms':perms,'perms_type':perms_type, 'perms_parent':perms_parent,'perms_url':perms_url,"perms_img":perms_img,"perms_method":perms_method}),
        success: function (data) {
            var ret = eval('(' + data + ')');
            if(ret.status =="perms_false"){
                spop({
                        template: ret.info,
                        style: 'warning',
                        autoclose: 3000
                    });
            }else {
                $("#edit-permsModal").modal("hide");
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


//删除权限
$("td a[name='del-perms']").click(function(){
    var perms_id = $(this).attr('perms_id');
    var statu = confirm("是否确认删除！");
    if (statu==true)
    {
        $.ajax({
            url: "/rbac/perms/",
            type: "DELETE",
            data: JSON.stringify({'perms_id':perms_id}),
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
