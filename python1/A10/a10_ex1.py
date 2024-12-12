import numpy as np

def matrix_operations(size: int) -> tuple:
    
    assert size > 0, "Size must be greater than 0."
    
    # 创建3D随机矩阵
    mat = np.random.randint(0, 100, (size, size, size))
    
    # 计算不同维度上的和
    axis_0_sum = np.sum(mat, axis=0)         # 沿0轴求和，结果是 (size, size)
    axis_01_sum = np.sum(mat, axis=(0, 1))   # 沿0,1轴求和，结果是 (size,)
    axis_all_sum = np.sum(mat)               # 沿所有轴求和，标量
    
    # 求最大值和最小值位置
    max_index = np.unravel_index(np.argmax(mat), mat.shape)
    min_index = np.unravel_index(np.argmin(mat), mat.shape)
    
    # 计算边界元素的和
    # 边界包括：所有在index=0或index=size-1的平面上的元素
    border_sum = (
        np.sum(mat[0, :, :]) + np.sum(mat[-1, :, :]) +
        np.sum(mat[1:-1, 0, :]) + np.sum(mat[1:-1, -1, :]) +
        np.sum(mat[1:-1, 1:-1, 0]) + np.sum(mat[1:-1, 1:-1, -1])
    )
    
    # Flatten and normalize
    flattened = mat.flatten().astype(float)
    if flattened.size > 0:
        normed_array = (flattened - np.min(flattened)) / (np.max(flattened) - np.min(flattened))
    else:
        normed_array = flattened
    
    return axis_0_sum, axis_01_sum, axis_all_sum, max_index, min_index, border_sum, normed_array

if __name__ == "__main__":
    # 测试样例（可自行注释或保留）
    np.random.seed(0)
    res = matrix_operations(3)
    for r in res:
        print(r)
    
    np.random.seed(0)
    res = matrix_operations(4)
    for r in res:
        print(r)