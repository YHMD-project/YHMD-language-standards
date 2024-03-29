"""
file: example.py
auther: yixing
"""
from base_assembly import Assembly
from base_component import Component

if __name__ == "__main__":
    # 创建回转轴装配线节点
    rotary_axis = Assembly("ex1_rotary_axis", "just a axis")
    # 添加第一个轴肩，此时一右边第一个作为初始轴肩
    rotary_axis.add_node(
        "_fixed",
        "null",
        Component("ex1_shoulder_1", "first shoulder"),
    )
    # 创建第二个轴肩节点
    shoulder_2 = Component("ex1_shoulder_2", "second shoulder")
    # 创建第二个轴肩的外表面装配线，并添加在第二个轴肩上
    sh2_external = Assembly(
        "ex1_sh2_external",
        "Outer surface of shaft shoulder 2",
    )
    # 在第二个轴肩的外表面装配线上添加退刀槽
    sh2_external.add_node(
        "_contain",
        ["_left", "ex1_shoulder_1"],  # 退刀槽在第一个轴肩左侧
        Component("groove", "tool withdrawal groove"),
    )
    # 将轴肩外表面装配线添加到第二个轴肩上
    shoulder_2.add_node(sh2_external)
    # 将第二个轴肩添加到回转轴装配线上
    rotary_axis.add_node(
        "_fixed",
        ["_left", "ex1_shoulder_1"],
        shoulder_2,
    )
    # 以下两种输出方式二选一
    # 单文件输出
    rotary_axis.output_to_json(
        "F:\\yixing_sub\\doing\\code\\YHMD-project\\YHMD-language-standards\\Examples\\example1\\jsonc\\example1.jsonc"
    )
    # 多文件输出
    rotary_axis.output_to_jsons(
        "F:\\yixing_sub\\doing\\code\\YHMD-project\\YHMD-language-standards\\Examples\\example1\\jsonc"
    )
