
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  def remove_child(parent, child_data):
    parent.children = [child for child in parent.children if child.data != child_data]

  def get_child(self, child_data):
    """ Obtiene el hijo con el nombre child_data solo de un nivel"""
    for child in self.children:
      if child.data == child_data:
        return child
    return None

  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    return level
  
  def print_tree(self):
    spaces = ' ' * self.get_level() * 3
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + str(self.data))
    if self.children:
      for child in self.children:
        child.print_tree()

# Probamos el código
def build_product_tree():
  root = TreeNode("Electronics")

  laptop = TreeNode("Laptop")
  laptop.add_child(TreeNode("Mac"))
  laptop.add_child(TreeNode("Surface"))
  laptop.add_child(TreeNode("Thinkpad"))

  cellphone = TreeNode("Cell Phone")
  cellphone.add_child(TreeNode("iPhone"))
  cellphone.add_child(TreeNode("Google Pixel"))
  cellphone.add_child(TreeNode("Vivo"))

  tv = TreeNode("TV")
  tv.add_child(TreeNode("Samsung"))
  tv.add_child(TreeNode("LG"))

  root.add_child(laptop)
  root.add_child(cellphone)
  root.add_child(tv)

  root.print_tree()

  # Obtenemo un nodo
"""   print("\n\n")
  node = cellphone.get_child("Vivo")
  if node:
    node.print_tree()
  else:
    print("Node not found") """

#build_product_tree()