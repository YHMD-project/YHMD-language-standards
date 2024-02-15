#

## 轴承

轴承一般为内部与轴配合、外部与外壳等配合，其内圈与外圈通常存在转速差，因此为了后续动力学分析方便，将其分为轴承内圈`inner_bearing`和轴承外圈`external_bearing`两个基础构件，这两个构件分别与其外部配合构件进行特定约束下的配合，相互之间则是特殊定义的轴承内外圈配合关系`withInnerRing`和`withExternalRing`

对于轴承内/外圈来说：
`type` 的值为 `inner_bearing`或`extenal_bearing`
`port` 中，除了轴承内外圈之间特殊定义的配合关系外，还有圆柱环的端口，分别为左侧、右侧、内包裹、外环绕、母线，需要注意的是轴承内圈无外环绕端口，轴承外圈无内包裹端口
`childassembly` 为子装配线节点，轴承固定的子装配线节点类型为 `rotary_axis`
