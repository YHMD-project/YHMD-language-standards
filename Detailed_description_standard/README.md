# readme

本文件夹主要给出机械描述标记语言标准

基本节点有两种： 装配线节点与构件节点

装配线节点不描述实体，而是描述其子构件的装配自由度和与子构件的装配关系。

构件节点表现为一个实体，其属性包括：材料、工艺、形貌尺寸、父装配线、子装配线。

构件节点一定是装配线节点的子节点。但是装配线的子节点还可以是装配线节点，这表示了装配线的重合。

* jsonc 中保留了当前标准下部分装配与节点会显示的结果
* spirit 中为以 python 实现的结构描述工具

需要保证在spirit中的对象输出为jsonc中同文件名下的jsonc文件

## jsonc

### 装配线节点

#### 节点属性

* "version" 标准版本号，尝试编写标准的阶段为 0 字头标准
* "name" 装配线节点的名称，自由定义
* "type" 装配线节点类型，只有**枚举值**
  * "rotary_axis" 回转轴系
  * "linear_axis" 直线轴系
  * $\dots$
* childComponents 子构件节点及链接方式列表
  * 列表中每个元素为一个字典，字典中包含两到三个键值对
    * "linkWithFa" 该节点与父节点的链接方式，只有**枚举值**，枚举值第一个字符为下划线
      * "_fixed" 固定，与父节点固连为一个整体
      * $\dots$
    * "linkWithBr" 该节点与兄节点的链接方式，只有**枚举值**，枚举值第一个字符为下划线
      * "_right" 在兄节点右侧
      * "_left" 在兄节点左侧
      * "_fixed" 与兄节点固连
      * $\dots$
    * "component" 子结构节点，如果该元素的值是字典，则直接展开；如果该元素的值是字符串，则表示该子节点的路径

### 构件节点

#### 节点属性

* "version" 标准版本号，尝试编写标准的阶段为 0 字头标准
* "name" 构件节点的名称，自由定义
* "brief" 构件节点的简要描述，自由定义
* "type" 构件节点类型，只有**枚举值**
  * "shaft_shoulder" 轴肩，与父节点必定为固连关系
  * "bearing" 轴承，与父节点必定为过盈关系
  * "axle_sleeve" 轴套
  * $\dots$
* "property" 构件节点属性，值是个字典
  * "materials" 材料，只有**枚举值**
  * "weight" 重量，单位为千克
  * "process" 工艺，只有**枚举值**
* "typeOfFatharassembly" 父装配线节点的类型，只有**枚举值**，枚举值与装配线节点的type相同
* "dimension" 构件节点的形貌尺寸，值是个字典，默认尺寸单位为毫米
  * "base" 描述构件的基本构型组，决定之后的参数类型
  * "diameter" 当base为圆柱时，存在直径属性
  * "length" 当base为圆柱时，存在母线长度属性
  * $\dots$
* "port" 构件节点端口，值是个字典，字典中值只有枚举值，描述弟节点可以的链接方式，枚举值与 "linkWithBr" 相同
* "childassembly" 子装配线节点，值是个列表，列表中每个元素为子装配线节点

#### 轴

根据收到的作用效果不同可以将轴分为三类:

* 转轴 既承受弯矩又承受转矩
* 心轴 只承受弯矩
* 传动轴 只承受转矩
* 什么都承受的为什么要放在这里呢

此处将回转轴理解为轴装配线上的一系列轴肩的固连组合，

首先可以写出一个回转轴为

```jsonc
{
    "name": "回转轴示例",
    "type": "rotary_axis",
}
```

`name` 标签为用户自定义的名称，`type` 的值为枚举类型，此处表示回转轴。

此时的轴是没有实体的，我们可以假设其由三个轴肩组成，

```jsonc
{
    "name": "回转轴示例",
    "type": "rotary_axis",
    "childComponents": [
        {
            "component": {
                "name": "轴肩1",
                "type": "shaft_shoulder"
            },
        },
        {
            "component": {
                "name": "轴肩2",
                "type": "shaft_shoulder",
            }
        }
        {
            "component": {
                "name": "轴肩3",
                "type": "shaft_shoulder"
            }
        }
    ]
}
```

补充各个轴肩的形貌尺寸

```jsonc
{
    "name": "回转轴示例",
    "type": "rotary_axis",
    "childComponents": [
        {
            "component": {
                "name": "轴肩1",
                "type": "shaft_shoulder",
                "dimension": {
                    "base": "cylinder",
                    "diameter": 10,
                    "length": 10
                },
            },
        },
        {
            "component": {
                "name": "轴肩2",
                "type": "shaft_shoulder",
                "dimension": {
                    "base": "cylinder",
                    "diameter": 20,
                    "length": 20
                },
            }
        }
        {
            "component": {
                "name": "轴肩3",
                "type": "shaft_shoulder"
                "dimension": {
                    "base": "cylinder",
                    "diameter": 30,
                    "length": 10
                },
            }
        }
    ]
}

我们还应该给出各个轴肩节点和父节点、兄弟节点、弟节点的链接方式，最终就可以得到一个完整的回转轴装配线。

```jsonc
{
    "name": "回转轴示例",
    "type": "rotary_axis",
    "childComponents": [
        {
            "linkWithFa": "_fixed",
            "component": {
                "name": "轴肩1",
                "type": "shaft_shoulder",
                "port": {
                    "rightPort": "_right",
                }
                "dimension": {
                    "base": "cylinder",
                    "diameter": 10,
                    "length": 10
                },
            },
        },
        {
            "linkWithFa": "_fixed",
            "linkWithBr": [
                "_right",
                "_fixed"
            ],
            "component": {
                "name": "轴肩2",
                "type": "shaft_shoulder",
                "port": {
                    "rightPort": "_right",
                }
                "dimension": {
                    "base": "cylinder",
                    "diameter": 20,
                    "length": 20
                },
            }
        }
        {
            "linkWithFa": "_fixed",
            "linkWithBr": [
                "_right",
                "_fixed"
            ],
            "component": {
                "name": "轴肩3",
                "type": "shaft_shoulder"
                "dimension": {
                    "base": "cylinder",
                    "diameter": 30,
                    "length": 10
                },
            }
        }
    ]
}
```

上面这段就表示在一个回转轴装配线上有三个轴肩，他们的长度分别为10, 20, 10，直径分别为10, 20, 30，他们之间彼此固连。

### 链接方式

#### 固连

#### 接触链接

#### 螺纹链接

#### 轴毂连接
