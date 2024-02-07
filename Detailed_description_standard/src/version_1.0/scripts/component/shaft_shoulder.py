"""
file: shaft_shoulder.py
auther: yixing

output like before
{
  "version": "0.1",
  "brief": "构件样例",
  "type": "shaft_shoulder",
  "name": "shoulder_2",
  "typeOfFatharassembly": "rotary_axis",
  "dimension": {
    "base": "cylinde",
    "diameter": "20mm",
    "length": "30mm"
  },
  "port": {
    "leftPort": "_left",
    "rightPort": "_right",
    "aroundPort": "_around",
    "cylindricalBus": "_bus"
  },
  "childassembly": {
    "axis": {
      "name": "axis_of_shoulder",
      "type": "rotary_axis",
      "childComent": {}
    }
  }
}

"""
from base_component import Component


class ShaftShoulder(Component):
    """class for discription of the shaft shoulder

    This class is base class for all the shaft shoulder
    这个类是所有轴肩的基类

    Parameters:
      verson: str, the version of the standard.
      type_of_component: str, "shaft_shoulder"
      type_of_father_assembly: str, "rotary_axis"

    Functions:
      init: This is the constructor of the class,
      output_to_json: Output recursively as a jsonc file.
      output_to_josns: Output recursively for each node as a jsonc file.
      add_node: Add a node to the component.
    """

    version = "0.1"
    type_of_component = "shaft_shoulder"
    type_of_father_assembly = "rotary_axis"

    def __init__(self, name, brief) -> None:
        """
        This is the constructor of the class.
        这是类的构造函数

        Parameter：
          name: str, the name of the component.
          brief: str, the brief description of the component.
          dimension: dict, the dimension of the component.

        Args:
          name: str, the name of the component.
          brief: str, the brief description of the component.

        Returns:
          None.
        """

        super().__init__(name, brief)

    def output_to_json(self, path: str) -> None:
        """
        Output recursively as a jsonc file.
        输出为一个完整文档

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """

    def add_node(self, node) -> None:
        """
        Add a node to the component.
        添加一个节点到构件

        Args:
          node: object, the node to be added.

        Returns:
          None.
        """
