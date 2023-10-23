# 定义一个二叉树结点的类
class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 列表构建二叉树
def build_tree(nodes):
    # 如果节点列表为空，返回 None
    if not nodes:
        return None
    # 构建根节点
    root = TreeNode(nodes[0])
    
    # 二叉树中节点的总个数
    for i in range(1,len(nodes)):
        d=TreeNode(nodes[i])
        p=root
        while True:
            if p.val<d.val:
                if p.left==None:
                    p.left=d
                    break
                else:
                    p=p.left
            else:
                if p.right==None:
                    p.right=d
                    break
                else:
                    p=p.right
    return root
# 前序遍历函数
def preorder(node):
    if node:
        preorder(node.left)
        print(node.val)    
        preorder(node.right)

# 反转二叉树
def invertTree(root):
    if not root:
        return root
    root.left = invertTree(root.left),
    root.right = invertTree(root.right)
    root.left,root.right =root.left,root.right
    return root

# 调用前序遍历函数
nodes = [45,4,32,23,331,2,3,56,90,888,43,4,5,55,7,5,22,13]
tree = build_tree(nodes)
inv_tree=invertTree(tree)
preorder(inv_tree)