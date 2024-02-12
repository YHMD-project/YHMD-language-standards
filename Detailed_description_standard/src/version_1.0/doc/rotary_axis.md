---
version: 1.0
author: yixing
---

#

## 回转轴系

回转轴系 `rotary_axis` 是相当经典的装配线结构

表示回转轴系的基装配线 或 回转构件的子装配线

`type` 的值为 `rotary_axis`

`dimension` 中 `diameter` 的值用于区分上述两种情况，如果 `diameter` 不存在 或 值为0 则表示基装配线，其子节点只能是与父节点固连的轴肩，否则表示回转构件的子装配线，其子节点的尺寸内径必然与该值相同。
