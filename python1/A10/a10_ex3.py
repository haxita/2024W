# a10_ex3.py
import numpy as np

def convolution(matrix: np.ndarray, kernel: np.ndarray, padding: int = 0) -> np.ndarray:
    
    assert matrix.ndim == 2, "matrix must be 2D"
    assert kernel.ndim == 2, "kernel must be 2D"
    
    m_h, m_w = matrix.shape
    k_h, k_w = kernel.shape
    
    assert k_h == k_w, "kernel must be square"
    assert k_h % 2 == 1, "kernel dimensions must be odd"
    assert m_h >= k_h and m_w >= k_w, "matrix must be larger than kernel"

    r = k_h // 2  # kernel半径
    total_padding = padding + r  # 总填充量（保证kernel可在边界对齐）
    
    padded_matrix = np.pad(matrix, ((total_padding, total_padding), (total_padding, total_padding)),
                           mode='constant', constant_values=0)
    
    output = np.zeros_like(matrix, dtype=float)
    
    # 卷积
    for i in range(m_h):
        for j in range(m_w):
            region = padded_matrix[i + total_padding - r : i + total_padding + r + 1,
                                   j + total_padding - r : j + total_padding + r + 1]
            output[i, j] = np.sum(region * kernel)
    
    return output

if __name__ == "__main__":
    np.random.seed(0)
    matrix = np.random.randint(0, 255, (32,32))
    kernel = np.ones((3,3)) * -1
    kernel[1,1] = 9
    print(convolution(matrix, kernel))