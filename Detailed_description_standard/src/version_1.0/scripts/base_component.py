"""
file: base_component.py
auther: yixing
"""
import json
import os
from base_node import BaseNode


class Component(BaseNode):
    """class for discription of the component

    This class is base class for all the component
    这个类是所有构件的基类

    Parameters:
      version: str, the version of the standard.
      type_of_component: str, the type of the component.
        "shaft_shoulder"
        "bearing"
        "axle_sleeve"
        ...
      type_of_father_assembly: str, the type of the father assembly.
        "rotary_axis"
        "linear_axis"

    Functions:

      init: This is the constructor of the class,
      output_to_json: Output recursively as a jsonc file.
      output_to_jsons: Output recursively for each node as a jsonc file.
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
        super().__init__(name, brief)
        self.dimension = {}
        self.port = {}
        self.child_assembly = []

    def output_to_dict(self) -> dict:
        """
        Output recursively as a dict.

        Args:
          None.

        Returns:
          dict.
        """
        self_dict = vars(self).copy()
        self_dict["child_assembly"] = []
        for child in self.child_assembly:
            self_dict["child_assembly"].append(child.output_to_dict())
        return self_dict

    def output_to_json(self, path: str) -> None:
        """
        Output recursively as a jsonc file.
        输出为一个完整文档

        Args:
          path: str, the path of the output file.

        Returns:
          None.
        """
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.output_to_dict(), f)
            print(f"output to {path} successfully")

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
        self_dict["child_assembly"] = []
        for child in self.child_assembly:
            child.output_to_jsons(folder_name)
            child_name = child.name
            child_path = os.path.join(folder_name, child_name + ".jsonc")
            self_dict["child_assembly"].append(child_path)

        with open(self_path, "w", encoding="utf-8") as f:
            json.dump(self_dict, f, indent=4)

        print(f"output to {self_path} successfully")

    def add_node(self, node) -> None:
        """
        Add a node to the component.
        添加一个节点到构件

        Args:
          node: object, the node to be added.

        Returns:
          None.
        """
        self.child_assembly.append(node)


if __name__ == "__main__":
    component_obj = Component("Component Name", "Component Description")
    component_obj_1 = Component("Component Name 1", "Component Description 1")
    component_obj.add_node(component_obj_1)
    component_obj.output_to_json("data/base_component.jsonc")
    component_obj.output_to_jsons("data")
