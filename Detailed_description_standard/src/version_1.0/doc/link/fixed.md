#

## 固连fixed

两个节点建模上实际上是一个整体，为了描述方面而被拆开时，将两者的连接方式定义为固连。

该方式允许的port对有`_right`、`_left`；`_inner_around`、`_external_around`（或`_around`）。

该方式可以额外具有的参数有`rotation`、`displacement`。`rotation`对于非回转体存在，表示两个节点基准的相对角度，定义由上级节点向下级节点方向看去，下级节点相对上级节点角度逆时针为正。`displacement`对于存在相交的节点，如螺纹，这个参数可以用来描述相交的深度，沿轴线插入为正。

```jsonc
{
    "port": "_right",
    "type": "_fixed",
    "rotation": 0,
    "displacement": 0
}
```
