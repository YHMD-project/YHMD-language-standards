#

## 接触contact

两个节点由圆柱面、平面等简单面接触进行链接。不同零件的配合许多可归为此类。

该方式允许的port对有`_right`、`_left`；`_inner_around`、`_external_around`（或`_around`）。

该方式可以额外具有的参数有`fit`。该参数描述的是配合公差，进而确定可动情况。可用的值有`_clearance`、`_transition`、`_close`。

```jsonc
{
    "port": "_right",
    "type": "_contact",
    "fit": "_clearance"
}
```
