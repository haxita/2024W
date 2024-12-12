# a10_ex4.py
import numpy as np

def one_hot_encoding(arr: np.ndarray) -> np.ndarray:
    if arr.ndim != 1:
        raise ValueError(f"The function can work for 1D matrices, not {arr.ndim}D")
    unique_values = np.unique(arr)
    # 对unique_values排序（np.unique本身已排序，但确保逻辑清晰）
    unique_values = np.sort(unique_values)
    # 创建映射字典
    value_to_index = {v:i for i,v in enumerate(unique_values)}
    
    # 创建编码数组
    encoded = np.zeros((arr.size, unique_values.size), dtype=float)
    for i, val in enumerate(arr):
        idx = value_to_index[val]
        encoded[i, idx] = 1.0
    return encoded

if __name__ == "__main__":
    a = np.array(["a","a","b","c"])
    print(one_hot_encoding(a))

    a = np.array([10,5,15,20])
    print(one_hot_encoding(a))

    a = np.array([[1, 2],[3,4]])
    try:
        print(one_hot_encoding(a))
    except ValueError as e:
        print(f"ValueError: {e}")