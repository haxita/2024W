import json
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import warnings

class TrainingSet():
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def to_json(self):
        return json.dumps(dict(
            type=self.__class__.__name__,
            X=self.X.tolist(),
            y=self.y.tolist()
        ))

    @staticmethod
    def from_json(jsonstring):
        data = json.loads(jsonstring)
        return TrainingSet.from_dict(data)
    
    @staticmethod
    def from_dict(data):
        return TrainingSet(
            np.array(data['X']).squeeze(),
            np.array(data['y'])
        )
    
    def plot_node_boundaries(self, node, limit_left, limit_right, limit_top, limit_bottom, max_depth, level=1):
        
        split_point = node.split_point
        limit_left_updated = limit_left
        limit_right_updated = limit_right
        limit_top_updated = limit_top
        limit_bottom_updated = limit_bottom

        if node.split_feature == 0:
            if limit_bottom == limit_top:
                warnings.warn('limit_bottom equals limit_top; extending by 0.1')
                plt.plot([split_point, split_point], [limit_bottom - 0.1, limit_top + 0.1], color="purple", alpha=1 / level)
            else:
                plt.plot([split_point, split_point], [limit_bottom, limit_top], color="purple", alpha=1 / level)
            limit_left_updated = split_point
            limit_right_updated = split_point

        else:
            if limit_left == limit_right:
                warnings.warn('limit_left equals limit_right; extending by 0.1')
                plt.plot([limit_left - 0.1, limit_right + 0.1], [split_point, split_point], color="purple", alpha=1 / level)
            else:
                plt.plot([limit_left, limit_right], [split_point, split_point], color="purple", alpha=1 / level)
            limit_top_updated = split_point
            limit_bottom_updated = split_point

        if level == max_depth:
            return
        if node.left_child is not None: self.plot_node_boundaries(node.left_child, limit_left, limit_right_updated,
                                                            limit_top_updated, limit_bottom, max_depth, level + 1)
        if node.right_child is not None: self.plot_node_boundaries(node.right_child, limit_left_updated, limit_right, limit_top,
                                                            limit_bottom_updated, max_depth, level + 1)
    
    def visualize(self, tree=None, max_height=None):
        symbols = [["x", "o"][index] for index in self.y]
        for y in set(self.y):
            X = self.X[self.y == y, :]
            plt.scatter(X[:, 0], X[:, 1],
                        color=["red", "blue"][y],
                        marker=symbols[y],
                        label="class: {}".format(y))
            
        if tree is not None:
            tree_height = tree.get_height(tree.root)
            if max_height is None or max_height > tree_height:
                max_height = tree_height
            self.plot_node_boundaries(tree.root, 
                                      limit_left=min(self.X[:, 0]),
                                      limit_right=max(self.X[:, 0]),
                                      limit_top=max(self.X[:, 1]),
                                      limit_bottom=min(self.X[:, 1]),
                                      max_depth=max_height) # TODO: make parameterizable

