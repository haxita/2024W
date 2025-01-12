from pig_lite.decision_tree.dt_node import DecisionTreeNodeBase
import scipy.stats as stats

def entropy(y: list):
    """
    Compute the entropy of a binary label distribution.

    This function calculates the entropy of a binary classification label list `y` as a wrapper 
    around `scipy.stats.entropy`. It assumes the labels are binary (0 or 1) and computes the 
    proportion of positive labels (1s) to calculate the entropy.

    Parameters
    ----------
    y : list
        A list of binary labels (0 or 1).

    Returns
    -------
    float
        The entropy of the label distribution. If the list is empty, returns 0.0.

    Notes
    -----
    - Entropy is calculated using the formula:
        H = -p*log2(p) - (1-p)*log2(1-p)
      where `p` is the proportion of positive labels (1s).
    - If `y` is empty, entropy is defined as 0.0.

    Examples
    --------
    >>> entropy([0, 0, 1, 1])
    1.0

    >>> entropy([1, 1, 1, 1])
    0.0

    >>> entropy([])
    0.0
    """
    if len(y) == 0: return 0.0
    positive = sum(y) / len(y)
    return stats.entropy([positive, 1 - positive], base=2)

# these two dummy classes are only used so we can import them and load trees from a pickle file before they are implemented by the students
class DecisionTree():
    def __init__(self) -> None:
        pass

    def get_height(self, node):
        if node is None:
            return 0
        return max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
    
    def print(self):
        if self.root is not None:
            height = self.get_height(self.root)
            self.root.print_tree(height)

class DecisionTreeNode(DecisionTreeNodeBase):
    def __init__(self) -> None:
        pass
