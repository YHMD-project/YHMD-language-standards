"""
file: example.py
auther: yixing
"""


class Component(object):
    """class for discription of the component

    This class is base class for all the component
    这个类是所有构件的基类

    Parameters:
      version: str, the version of the standard.
      type_of_component: str, the type of the component.
      type_of_father_assembly: str, the type of the father assembly.

    Functions:

      init: This is the constructor of the class,
      output_to_json: Output recursively as a jsonc file.
      output_to_josns: Output recursively for each node as a jsonc file.
      add_node: Add a node to the component.
    """

    version = "0.1"
    type_of_component = ""
    type_of_father_assembly = ""

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

        self.name = name
        self.brief = brief
        self.dimension = {}
        self.port = {}
        self.child_assembly = []

    def output_to_json(self, path: str) -> None:
        """
        Output recursively as a jsonc file.
        输出为一个完整文档

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """

    def output_to_josns(self, path: str) -> None:
        """
        Output recursively for each node as a jsonc file.
        输出为一个文件夹，将每个装配节点和构件节点分别输出为文件

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


class Assmbly(object):
    """class for discription of the assembly

    This class is base class for all the assembly
    这个类是所有装配线的基类

    Parameters:
      verson: str, the version of the standard.
      type_of_assemnly: str, the type of the assembly.

    Functions:

      init: This is the constructor of the class,
      output_to_json: Output recursively as a jsonc file.输出为一个完整文档
      output_to_josns: Output recursively for each node as a jsonc file.
                       输出为一个文件夹，将每个装配节点和构件节点分别输出为文件
      add_node: Add a node to the assembly.添加一个节点到装配线
    """

    version = "0.1"
    type_of_assemnly = ""

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

        self.name = name
        self.brief = brief
        self.child_component = []

    def link_to_json(self, link_with_fa, link_with_br) -> None:
        """
        Link the assembly to the json file.
        将装配线链接到json文件

        Args:
          link_with_fa: str, the link type with father node.
          link_with_br: str, the link type with brother node.

        Returns:
          json_string: str, jsonc string of self.
        """

    def output_to_json(self, path: str) -> None:
        """
        Output recursively as a jsonc file.
        输出为一个完整文档

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """

    def output_to_josns(self, path: str) -> None:
        """
        Output recursively for each node as a jsonc file.
        输出为一个文件夹，将每个装配节点和构件节点分别输出为文件

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """

    def add_node(self, node) -> None:
        """
        Add a node to the assembly.
        添加一个节点到装配线

        Args:
          node: object, the node to be added.

        Returns:
          None.
        """


class RotaryAxis(Assmbly):
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
