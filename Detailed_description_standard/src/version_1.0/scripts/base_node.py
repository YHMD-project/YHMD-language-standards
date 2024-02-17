"""
file: base_node.py
auther: yixing
"""


class BaseNode(object):
    """class for discription of the node

    This class is base class for all the node
    这个类是所有节点的基类

    Parameters:
      version: str, the version of the standard.

    Functions:
      init: This is the constructor of the class,
      output_to_json: Output recursively as a jsonc file.
      output_to_jsons: Output recursively for each node as a jsonc file.
      add_node: Add a node to the node.
    """

    version = "0.1"

    def __init__(self, name, brief) -> None:
        """
        This is the constructor of the class.
        这是类的构造函数

        Parameter：
          name: str, the name of the node.
          brief: str, the brief description of the node.

        Args:
          name: str, the name of the node.
          brief: str, the brief description of the node.

        Returns:
          None.
        """

        self.name = name
        self.brief = brief

    def output_to_json(self, path: str) -> None:
        """
        Output recursively as a jsonc file.
        输出为一个完整文档

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """

    def output_to_jsons(self, path: str) -> None:
        """
        Output recursively for each node as a jsonc file.
        输出为一个文件夹，将每个装配节点和构件节点分别输出为文件

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """
