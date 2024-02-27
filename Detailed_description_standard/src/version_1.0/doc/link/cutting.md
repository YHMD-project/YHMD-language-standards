#

## 实体切割cutting

这种链接方式用于在实体上增加负实体来实现螺纹、键槽等结构。

该方式允许的port对有`_bus`、`_cutting`。

该方式可以额外具有的参数有`rotation`、`departure`。`rotation`对于没有严格旋转对称的实体存在，表示新增切除关于之前实体所定义的极轴位置（比如已经存在的键槽）的偏移角，逆时针为正；`departure`参数描述了两实体在母线方向错开的距离，用以进行轴向定位。该参数为 0 时，恰好端端对齐。

```jsonc
{
    "port": "_bus",
    "type": "_cutting",
    "rotation": 0,
    "departure": 0
}
```
