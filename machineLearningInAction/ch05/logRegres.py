from numpy import mat, shape, ones, exp


def load_data_set():
    data_mat = []
    label_mat = []
    fr = open('testSet.txt')
    while True:
        line = fr.readline()
        if line == '':
            break
        line_arr = line.strip().split()
        data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
        label_mat.append(int(line_arr[2]))
    return data_mat, label_mat


def sigmoid(in_x):
    return 1.0 / (1 + exp(-in_x))


def grad_ascent(data_mat_in, class_labels):
    data_matrix = mat(data_mat_in)  # 把数组转换为矩阵
    label_mat = mat(class_labels).transpose()
    m, n = shape(data_matrix)
    alpha = 0.001
    max_cycles = 500
    weights = ones((n, 1))
    for k in range(max_cycles):
        h = sigmoid(data_matrix * weights)
        error = (label_mat - h)
        weights = weights + alpha * data_matrix.transpose() * error
    print(weights)
    return weights


data_arr, label_mat = load_data_set()
grad_ascent(data_arr, label_mat)
