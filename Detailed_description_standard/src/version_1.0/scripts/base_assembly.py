"""
file: base_assembly.py
auther: yixing
"""
import json
import os
from base_node import BaseNode


class Assembly(BaseNode):
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
      output_to_jsons: Output recursively for each node as a jsonc file.
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
              "component": a list of a dict,each dict discribe a component and
                its link type with the assembly.
            }

        Args:
          name: str, the name of the assembly.
          brief: str, the brief description of the assembly.

        Returns:
          None.
        """
        super().__init__(name, brief)
        self.child_component = []

    def output_to_dict(self) -> dict:
        """
        Output recursively as a dict.

        Args:
          None.

        Returns:
          dict of the assembly.
        """
        self_dict = vars(self).copy()
        for child, child_dict in zip(
            self.child_component, self_dict["child_component"]
        ):
            child_dict["component"] = child["component"].output_to_dict()
        return self_dict

    def output_to_json(self, path: str = ""):
        """
        Output recursively as a jsonc file.
        输出为一个完整文档

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.output_to_dict(), f, indent=4)
            print(f"Output to {path} successfully.")

    def output_to_jsons(self, path: str) -> None:
        """
        Output recursively for each node as a jsonc file.
        输出为一个文件夹，将每个装配节点和构件节点分别输出为文件

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """
        folder_name = os.path.join(path, self.name)
        self_path = os.path.join(folder_name, self.name + ".jsonc")
        os.makedirs(folder_name, exist_ok=True)
        self_dict = vars(self).copy()
        for child, child_dict in zip(
            self.child_component, self_dict["child_component"]
        ):
            child["component"].output_to_jsons(folder_name)
            child_name = child["component"].name
            child_path = os.path.join(folder_name, child_name + ".jsonc")
            child_dict["component"] = child_path

        with open(self_path, "w", encoding="utf-8") as f:
            json.dump(self_dict, f, indent=4)

        print(f"Output to {self_path} successfully.")

    def add_node(self, link_with_fa, link_with_br, node) -> None:
        """
        Add a node to the assembly.
        添加一个节点到装配线

        Args:
          node: object, the node to be added.

        Returns:
          None.
        """
        self.child_component.append(
            {
                "link_with_fa": link_with_fa,
                "link_with_br": link_with_br,
                "component": node,
            }
        )


if __name__ == "__main__":
    assembly_obj = Assembly("Assembly Name", "Assembly Description")
    assembly_obj_1 = Assembly("Assembly Name 1", "Assembly Description 1")
    assembly_obj.add_node(
        "link_with_fa",
        "link_with_br",
        assembly_obj_1,
    )
    assembly_obj.output_to_json("data/bass_assembly.jsonc")
    assembly_obj.output_to_jsons("data")
