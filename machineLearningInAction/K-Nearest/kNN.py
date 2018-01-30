from numpy import *
import operator
import matplotlib.pyplot as plt


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# data_set为传入的矩阵数组,labels为类别,k标示为矩阵的维度,in_x为标准数组
def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_dist_indicies = distances.argsort()
    # 初始化一个set
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_dist_indicies[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1
    # 对clas_count做排序,key=operator.itemgetter(1)表示取第二个元素做key,也可以对对象取属性名做key:attrgetter
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def file2matrix(filename):
    fr = open(filename)
    array_o_lines = fr.readlines()
    number_of_lines = len(array_o_lines)
    return_mat = zeros((number_of_lines, 3))
    class_label_vector = []
    index = 0
    for line in array_o_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        # print(list_from_line)
        # 取第0-3个元素
        return_mat[index, :] = list_from_line[0:3]
        # print(return_mat)
        class_label_vector.append(int(list_from_line[-1]))
        index += 1
    return return_mat, class_label_vector


# 对数值做归一化处理
def auto_norm(data_set):
    # 从第一列中获取最小值
    min_val = data_set.min(0)
    max_val = data_set.max(0)
    ranges = max_val - min_val
    m = data_set.shape[0]
    # tile将变量内容复制成输入矩阵同样大小的矩阵
    norm_data_set = data_set - tile(min_val, (m, 1))
    # 每个特征值相除,矩阵相除应该使用linalg.solve函数
    norm_data_set = norm_data_set / tile(ranges, (m, 1))
    return norm_data_set, ranges, min_val


def print_matrix():
    dating_data_mat, dating_labels = file2matrix('test/datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('game time percent')
    ax.set_ylabel('ice cream quantity')
    print('dating_data_mat:', dating_data_mat)
    # print(dating_labels)
    # 第二列数据和第三列数据分别表示两个变量,这里取这两个变量分别表示横坐标和纵坐标
    # ax.scatter(dating_data_mat[:, 1], dating_data_mat[:, 2])
    norm_mat, ranges, min_value = auto_norm(dating_data_mat)
    print('norm_mat:', norm_mat)
    # 前两个分别代表横坐标和纵坐标,后两个分别代表形状和颜色
    ax.scatter(norm_mat[:, 1], norm_mat[:, 2], 15 * array(dating_labels), array(dating_labels))
    plt.show()


def dating_class_test():
    ho_ratio =0.1
    dating_data_mat, dating_labels = file2matrix('test/datingTestSet2.txt')
    norm_mat, ranges, min_vals = auto_norm(dating_data_mat)
    # shape取矩阵的维度,shape[0]获取到行数
    m = norm_mat.shape[0]
    num_test_vecs = int(m * ho_ratio)
    print("norm_mat:", norm_mat)
    error_count = 0.0
    for i in range(num_test_vecs):
        # 通过classify0方法对传入的矩阵做分类,分类结果为classifier_result
        print("in_x:", norm_mat[i, :])
        print("data_set:", norm_mat[num_test_vecs:m, :])
        # 对矩阵的从第num_test_vecs行之后的数据做测试,测试num_test_vecs次,每次测试的基准值为第i行的数据
        classifier_result = classify0(norm_mat[i, :], norm_mat[num_test_vecs:m, :], dating_labels[num_test_vecs:m], 3)
        print("the classifier came back with:%d,the real answer is:%d" % (classifier_result, dating_labels[i]))
        if (classifier_result != dating_labels[i]):
            error_count += 1.0
    print("total error rate:%f" % (error_count / float(num_test_vecs)))


# group, labels = create_data_set()
# print(classify0([1, 1], group, labels, 3))
# print_matrix()
dating_class_test()
