////////////////脚本//////////////////

//删除环境
$("td a[name='del-server']").click(function(){
   var server_id = $(this).attr('server_id');
   var statu = confirm("是否确认删除！");
   if (statu==true)
    {
        $.ajax({
            url: "/sys/install/",
            type: "DELETE",
            data: JSON.stringify({'server_id':server_id}),
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