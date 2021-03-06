from math import log


# 计算熵
def calc_shanno_ent(data_set):
    num_entries = len(data_set)
    label_counts = {}
    for feat_vec in data_set:
        # [-1]表示取数组的最后一个元素
        current_label = feat_vec[-1]
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
        label_counts[current_label] += 1
    shannon_ent = 0.0
    for key in label_counts:
        # 计算每个label的概率
        prob = float(label_counts[key] / num_entries)
        shannon_ent -= prob * log(prob, 2)
    print(shannon_ent)
    return shannon_ent


def split_date_set(data_set, axis, value):
    ret_data_set = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduce_feat_vec = feat_vec[:axis]
            reduce_feat_vec.extend(feat_vec[axis + 1:])
    print(ret_data_set)
    return ret_data_set


def create_data_set():
    data_set = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return data_set, labels


mat, labels = create_data_set()
# calc_shanno_ent(mat)
split_date_set(mat, 0, 1)
