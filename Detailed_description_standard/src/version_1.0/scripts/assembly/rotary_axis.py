"""
file: rotary_axis.py
auther: yixing

output like before
{
  "version": "0.1",
  "brief": "轴系装配线样例",
  "name": "rotary axis system",
  "type": "rotary_axis",

  "childComponent": [
    {
      "linkWithFa": "_fixed",
      "component": {
        "name": "shaft_shoulder_1"
      }
    },
    {
      "linkWithFa": "_fixed",
      "linkwithBr": [
        "_right",
        "_fixed",
        "shaft_shoulder_1"
      ],
      "component": "PATH-TO-FILE/shoulder_2.jsonc"
    }
  ]
}

"""

from base_assembly import assembly


class RotaryAxis(assembly):
    """class for discription of the rotary axis

    This class is base class for all the rotary axis
    这个类是旋转轴装配线的基类
    Parameters:
      verson: str, the version of the standard.
      type_of_assemnly: "rotary_axis"

    Functions:
      init: This is the constructor of the class,
      link_to_json: Link the assembly to the json file.
      output_to_json: Output recursively as a jsonc file.输出为一个完整文档
      output_to_josns: Output recursively for each node as a jsonc file.
                       输出为一个文件夹，将每个装配节点和构件节点分别输出为文件
      add_node: Add a node to the assembly.添加一个节点到装配线
    """

    version = "0.1"
    type_of_assemnly = "rotary_axis"

    def __init__(self, name, brief) -> None:
        """
        This is the constructor of the class.
        这是类的构造函数

        Parameter：
          name: str, the name of the assembly.
          brief: str, the brief description of the assembly.
          child_component: dict, the child component of the assembly.
            {
              "link_with_fa": str, the link type with father node.
              "link_with_br": str, the link type with brother node.
              "component": Component class, the component of the assembly.
            }

        Args:
          name: str, the name of the assembly.
          brief: str, the brief description of the assembly.

        Returns:
          None.
        """

        super().__init__(name, brief)
