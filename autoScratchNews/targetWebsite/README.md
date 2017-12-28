{
  //指定某个网站
  "url": "blog.coderhelper.cn",
  //通过该定位元素，判断是否进行以后操作
  "IndexPosition": "tag.class.className***tag2.id.idName",
  //如果上述元素获取的值，符合我们爬取的要求，那么获取接下来的source
  "sourcePosition": "tag.class.className***tag2.id.idNmae",


  //above source content will abstraction URL stored in URL pool
  //这个是设置该网址爬取内容，各部分权重部分
  "contentWeight":{
    "section1":"xxx"
  }
  //如果自己不想设置权重，我们内嵌有默认最优权重配置
  "contentWeight":"default"
}
