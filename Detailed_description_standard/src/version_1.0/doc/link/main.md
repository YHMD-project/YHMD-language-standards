#

## 总述

节点与兄节点的链接方式如下定义。`brName`为兄节点名称；`brLink`是一个字典，其中必须含有`port`、`type`两个键和对应的值，还可根据`type`的值含有不同的链接描述参数。非必要的键值对可以缺省，缺省时其值可以默认为0。
`port`是兄节点与自身参与链接的端口，应与`type`匹配。`type`为链接方式，决定了后续的键值对内容与数量。
与父节点的连接方式和与兄节点的连接方式基本一致。

```jsonc
"linkwithBr": [
    // linkwithBr 的值是一个列表，依次表示与兄弟节点的关系
    {
        "brName": "shaft_shoulder_1",
        "brLink": 
        {
            "port": "_right",
            "type": "_fixed",
            "rotation": 0
        }
    }
],
```

```jsonc
"linkwithFa": [
    {
        "faName": "rotary_axis_example",//为了方便父节点与兄节点解析的一致，这里不取消父节点名称
        "faLink": 
        {
            "port": "_right",
            "type": "_fixed",
            "rotation": 0
        }
    }
],
```

具体的`type`定义在其余文件中一一展示。
