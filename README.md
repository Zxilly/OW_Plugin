# OW-Plugin
在网页上展示你的守望先锋战绩

![demo1](https://ow.plugin.learningman.top/api/84ef39db28e2169e31dc8bbff4ad527f.svg)

## 使用方法
打开[守望先锋战绩查询](https://ow.blizzard.cn/career/) ，在控制台执行 
```javascript
$.ajax({url:"/action/career/profile?"+(new Date).getTime(),type:"GET",dataType:"text",success:function(a){$.ajax({url:"https://ow.plugin.learningman.top/update",type:"POST",data:JSON.stringify({"data":a}),success:function(b){console.log(b)}})}});
```
生成的战绩图片会显示在下一行

战绩数据如果有变动需要手动更新，战绩图片地址不变，因为暴雪的登陆验证实在是太严格了）

你可以在`expired`分支找到爬虫相关的代码，如果能帮我优化一下非常感谢，主要缺少的是处理`challenge`相关的代码
