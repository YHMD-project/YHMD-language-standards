class assembly(object):
    """class for discription of the assembly

    This class is base class for all the assembly
    这个类是所有装配线的基类

    Parameters:
      verson: str, the version of the standard.
      type_of_assemnly: str, the type of the assembly.
        "rotary_axis"
        "linear_axis"
        ...

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
