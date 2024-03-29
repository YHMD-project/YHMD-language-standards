---
version: 1.0
author: yixing
---

# 构件节点

## 总述

这是构件节点的说明文档。

构件节点是描述机械结构的最小单元，每个构件都表示为一个实体，需要注意的是通过 `_fixed` 连接的实体被认为是同一个实体。

构件节点所代表的实体有正实体和负实体之分，负实体的部分不会绘制在图纸和模型中，而且会去除与正实体装配过程中重合的部分，实际表现在加工过程中就是减材加工，像是开槽、开孔、开螺纹等。

描述构件就是在描述实体，故而尺寸、父节点接口、弟节点接口等都是构件节点的重要属性。

### 构件节点的 jsonc 描述

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
* "typeOfFatherAssembly" 父装配线节点的类型，只有**枚举值**，枚举值与装配线节点的type相同
* "dimension" 构件节点的形貌尺寸，值是个字典，默认尺寸单位为毫米
  * "base" 描述构件的基本构型组，决定之后的参数类型
  * "diameter" 当base为圆柱时，存在直径属性
  * "length" 当base为圆柱时，存在母线长度属性
  * $\dots$
* "port" 构件节点端口，值是个列表，列表的每个值是个字典，字典中值只有枚举值，描述弟节点可以的链接方式，枚举值与 "linkWithBr" 相同
* "childassembly" 子装配线节点，值是个列表，列表中每个元素为子装配线节点

@import "jsonc\shaft_shoulder.md"
@import "jsonc\bearing.md"
@import "jsonc\cylindrical_groove.md"
@import "jsonc\keyway.md"
@import "jsonc\shaft_shoulder.md"
@import "jsonc\shaft_sleeve.md"
