from avl_node import AVLNode


class AVLTree:
    class NodeGroup:
        def __init__(self):
            self.a = None
            self.b = None
            self.c = None
            self.t0 = None
            self.t1 = None
            self.t2 = None
            self.t3 = None

    def __init__(self):
        self.root = None
        self.size = 0
        self.to_restruct = None

    def getTreeRoot(self):
        """
        获取 AVL 树的根节点
        :return: AVLNode -- AVL 树的根节点
        """
        return self.root  # 返回根节点

    def getTreeHeight(self):
        """获取 AVL 树的高度。
        :return: -1（空树）或当前树的高度。
        """
        if self.root is None:
            return -1  # 空树高度为 -1
        else:
            return self.root.height  # 返回根节点的高度

    def getSize(self):
        """返回树中键/值对的数量。
        :return: 键/值对的数量。
        """
        return self.size  # 返回节点数量

    def find_by_key(self, key):
        """根据给定的键返回节点的值。
        :param key: 要搜索的键。
        :return: 如果找到键，返回对应的值，否则返回 None。
        :raises ValueError: 如果键为 None。
        """
        if key is None:
            raise ValueError("Cannot search for null key!")
        current = self.root
        while current is not None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left

        return None

    # 辅助函数：更新节点高度
    def update_height(self, node):
        """
        更新节点的高度。

        节点的高度等于左右子树高度的最大值加 1。

        :param node: 要更新高度的节点。
        """
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        node.height = max(left_height, right_height) + 1  # 更新节点高度

    # 辅助函数：计算节点的平衡因子
    def get_balance(self, node):
        """
        计算节点的平衡因子。

        平衡因子等于左子树高度减去右子树高度。

        :param node: 要计算平衡因子的节点。
        :return: 平衡因子。
        """
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height
        return left_height - right_height  # 返回平衡因子

    # 左旋操作
    def left_rotate(self, x):
        """
        对节点 x 进行左旋操作。

        左旋示意图：
            x                     y
             \                   / \
              y      ---->      x   T3
             / \               / \
           T2  T3            T1  T2

        :param x: 要进行左旋的节点。
        """
        y = x.right  # y 为 x 的右子节点
        T2 = y.left  # T2 为 y 的左子树

        # 执行旋转
        y.left = x
        x.right = T2

        # 更新父节点关系
        y.parent = x.parent
        if x.parent is None:
            self.root = y  # 如果 x 是根节点，更新根节点
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        x.parent = y
        if T2 is not None:
            T2.parent = x

        # 更新节点高度
        self.update_height(x)
        self.update_height(y)

    # 右旋操作
    def right_rotate(self, y):
        """
        对节点 y 进行右旋操作。

        右旋示意图：
                y                 x
               /                 / \
              x       ---->     T1  y
             / \                   / \
           T1  T2                T2  T3

        :param y: 要进行右旋的节点。
        """
        x = y.left  # x 为 y 的左子节点
        T2 = x.right  # T2 为 x 的右子树

        # 执行旋转
        x.right = y
        y.left = T2

        # 更新父节点关系
        x.parent = y.parent
        if y.parent is None:
            self.root = x  # 如果 y 是根节点，更新根节点
        else:
            if y.parent.left == y:
                y.parent.left = x
            else:
                y.parent.right = x
        y.parent = x
        if T2 is not None:
            T2.parent = y

        # 更新节点高度
        self.update_height(y)
        self.update_height(x)

    def insertNode(self, key, value):
        """插入一个新节点到 AVL 树中。
        :param key: 新节点的键。
        :param value: 新节点的数据。必须不为 None。键不能重复，如果重复返回 False。键和值不能为 None，否则抛出错误。
        :return: 如果插入成功返回 True，否则返回 False。
        :raises ValueError: 如果键或值为 None。
        """
        if key is None:
            raise ValueError("Null keys are not allowed!")

        if self.root is None:
            self.root = AVLNode(key, value)
            self.size += 1
            # 新插入的节点是根节点，无需调整
            return True
        else:
            current = self.root
            while True:
                if current.key == key:
                    return False
                elif current.key < key:
                    if current.right is not None:
                        current = current.right
                    else:
                        new_node = AVLNode(key, value)
                        self.set_right(current, new_node)
                        break
                else:
                    if current.left is not None:
                        current = current.left
                    else:
                        new_node = AVLNode(key, value)
                        self.set_left(current, new_node)
                        break
        self.size += 1
        # TODO update heights, check AVL integrity, restructure if needed

        # 从新插入的节点开始，向上回溯，更新高度并检查平衡
        node = new_node
        while node is not None:
            self.update_height(node)  # 更新当前节点高度
            balance = self.get_balance(node)  # 计算当前节点的平衡因子

            # 检查节点是否失衡
            if balance > 1:
                if self.get_balance(node.left) >= 0:
                    # LL 情况，右旋转
                    self.right_rotate(node)
                else:
                    # LR 情况，先对左子节点进行左旋转，再对当前节点进行右旋转
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif balance < -1:
                if self.get_balance(node.right) <= 0:
                    # RR 情况，左旋转
                    self.left_rotate(node)
                else:
                    # RL 情况，先对右子节点进行右旋转，再对当前节点进行左旋转
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent  # 向上回溯到父节点

        return True

    def removeNode(self, key):
        """根据给定的键删除节点。
        :param key: 要删除的节点的键。
        :return: 如果找到并删除节点返回 True，否则返回 False。
        :raises ValueError: 如果键为 None。
        """
        if key is None:
            raise ValueError("Null key is not allowed!")

        parent = None
        current = self.root
        new_sub_root = None

        while not (current is None):
            if current.key == key:
                if parent is None:
                    self.root = self._remove_bst(current)
                    if self.root is not None:
                        self.root.parent = None
                elif parent.left == current:
                    new_sub_root = self._remove_bst(current)
                    self.set_left(parent, new_sub_root)
                elif parent.right == current:
                    new_sub_root = self._remove_bst(current)
                    self.set_right(parent, new_sub_root)
                else:
                    raise ValueError()

                self.size -= 1
                # to_restruct 是我们需要开始调整的节点
                if self.to_restruct is not None:
                    # TODO update heights
                    node = self.to_restruct
                    while node is not None:
                        self.update_height(node)  # 更新当前节点高度
                        balance = self.get_balance(node)  # 计算平衡因子

                        # 检查节点是否失衡
                        if balance > 1:
                            if self.get_balance(node.left) >= 0:
                                # LL 情况，右旋转
                                self.right_rotate(node)
                            else:
                                # LR 情况，先对左子节点进行左旋转，再对当前节点进行右旋转
                                self.left_rotate(node.left)
                                self.right_rotate(node)
                        elif balance < -1:
                            if self.get_balance(node.right) <= 0:
                                # RR 情况，左旋转
                                self.left_rotate(node)
                            else:
                                # RL 情况，先对右子节点进行右旋转，再对当前节点进行左旋转
                                self.right_rotate(node.right)
                                self.left_rotate(node)
                        node = node.parent  # 向上回溯到父节点

                return True
            else:
                parent = current
                if current.key > key:
                    current = current.left
                else:
                    current = current.right

        return False

    # 辅助函数：删除 BST 中的节点
    def _remove_bst(self, old_sub_root):
        new_sub_root = None
        if old_sub_root.left is None and old_sub_root.right is None:
            # 被删除的节点是叶子节点
            new_sub_root = None
            self.to_restruct = old_sub_root.parent  # 从父节点开始调整
        elif old_sub_root.left is None:
            # 被删除的节点只有右子节点
            new_sub_root = old_sub_root.right
            self.to_restruct = new_sub_root  # 从替换节点开始调整
        elif old_sub_root.right is None:
            # 被删除的节点只有左子节点
            new_sub_root = old_sub_root.left
            self.to_restruct = new_sub_root  # 从替换节点开始调整
        elif old_sub_root.left.right is None:
            # 左子节点没有右子节点
            new_sub_root = old_sub_root.left
            self.set_right(new_sub_root, old_sub_root.right)
            self.to_restruct = new_sub_root  # 从替换节点开始调整
        elif old_sub_root.right.left is None:
            # 右子节点没有左子节点
            new_sub_root = old_sub_root.right
            self.set_left(new_sub_root, old_sub_root.left)
            self.to_restruct = new_sub_root  # 从替换节点开始调整
        else:
            # 找到前驱节点替换
            new_sub_root = old_sub_root.left
            while new_sub_root.right is not None:
                new_sub_root = new_sub_root.right
            predecessor_p = new_sub_root.parent
            self.set_right(predecessor_p, new_sub_root.left)
            self.set_right(new_sub_root, old_sub_root.right)
            self.set_left(new_sub_root, old_sub_root.left)
            self.to_restruct = predecessor_p  # 从前驱节点的父节点开始调整

        return new_sub_root

    def set_left(self, parent, child):
        parent.left = child
        if child is not None:
            child.parent = parent

    def set_right(self, parent, child):
        parent.right = child
        if child is not None:
            child.parent = parent