from numpy import array
from numpy import log
from numpy import ones
from numpy import random


def load_data_set():
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]
    return posting_list, class_vec


def create_vocab_list(data_set):
    vocab_set = set([])
    for document in data_set:
        # 取两个集合的并集
        vocab_set = vocab_set | set(document)
    return list(vocab_set)
    # return ['quit', 'buying', 'mr', 'licks', 'mr']


# vocab_list是一个要测试的文件，input_set则是其中一个训练好的标准数组。这个方法用来将文本转换为数字，转换标准为：input_set中有的单词，
# 在要测试的文件中标示为1，不存在的为0.最终将要加工的文件转换为只包含0和1的数组
# 这个方法存在的问题是测试文件不能包含重复的单词，否则后边重复的单词不会被匹配。
def set_of_words2_vec(vocab_list, input_set):
    return_vec = [0] * len(vocab_list)  # 生成一个包含指定长度的数组
    for word in input_set:
        if word in vocab_list:
            return_vec[vocab_list.index(word)] = 1
        else:
            print("the wojrd:%s is not in my vocabulary", word)
    return return_vec


def train_nb_0(train_matrix, train_category):
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    p_abusive = sum(train_category) / float(num_train_docs)  # 代表划分为类别1的样本占总样本的比例（0.5）
    p0_num = ones(num_words)
    p1_num = ones(num_words)
    p0_denom = 2.0
    p1_denom = 2.0
    for i in range(num_train_docs):
        if train_category[i] == 1:
            p1_num += train_matrix[i]
            p1_denom += sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_denom += sum(train_matrix[i])
    print('p0_num:', p0_num)
    print('p1_num:', p1_num)
    p1_vect = log(p1_num / p1_denom)  # 对概率值取对数
    p0_vect = log(p0_num / p0_denom)
    return p0_vect, p1_vect, p_abusive


# p0_vec对应各个单词属于类别0的概率；vec2_classify对应测试样本转换为数字后的数组
# p0和p1分别对应各个单词位于类别0和1的概率之和
def classify_nb(vec2_classify, p0_vec, p1_vec, p_class1):
    print('classify_nb:', vec2_classify)
    print('classify_nb:', p0_vec)
    print('classify_nb:', p1_vec)
    p1 = sum(vec2_classify * p1_vec) + log(p_class1)
    p0 = sum(vec2_classify * p0_vec) + log(1.0 - p_class1)
    if p1 > p0:
        return 1
    else:
        return 0


def testing_nb():
    list_o_posts, list_classes = load_data_set()
    my_vocab_list = create_vocab_list(list_o_posts)
    train_mat = []
    for postin_doc in list_o_posts:
        train_mat.append(set_of_words2_vec(my_vocab_list, postin_doc))
    p0_v, p1_v, p_ab = train_nb_0(array(train_mat), array(list_classes))

    test_entry = ['love', 'my', 'dalmation']
    this_doc = array(set_of_words2_vec(my_vocab_list, test_entry))  # 转成数字的测试样本
    print(test_entry, 'classified as:', classify_nb(this_doc, p0_v, p1_v, p_ab))
    test_entry = ['stupid', 'garbage']
    this_doc = array(set_of_words2_vec(my_vocab_list, test_entry))
    print(test_entry, 'classified as:', classify_nb(this_doc, p0_v, p1_v, p_ab))


# testing_nb()
def text_parse(big_string):
    import re
    list_of_tokens = re.split(r'\W*', big_string)
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]


# spam下的是垃圾邮件，而ham下为正常邮件。随机选取10个邮件作为训练数据，剩余的邮件作为测试数据。对于选取的10个训练数据，通过beyes分类计算每个单词的概率之后，对测试数据做分类。
def spam_test():
    doc_list = []
    class_list = []
    full_text = []
    for i in range(1, 26):
        word_list = text_parse(open('email/spam/%d.txt' % i).read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)
        word_list = text_parse(open('email/ham/%d.txt' % i).read())
        doc_list.append(word_list)
        class_list.append(0)
        full_text.extend(word_list)
    vocab_list = create_vocab_list(doc_list)
    training_set = list(range(50))
    test_set = []
    for i in range(10):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del (training_set[rand_index])
    train_mat = []
    train_classes = []
    for doc_index in training_set:
        train_mat.append(set_of_words2_vec(vocab_list, doc_list[doc_index]))
        train_classes.append(class_list[doc_index])
    p0_v, p1_v, p_span = train_nb_0(train_mat, array(train_classes))
    error_count = 0
    for doc_index in test_set:
        word_vector = set_of_words2_vec(vocab_list, doc_list[doc_index])
        if classify_nb(array(word_vector), p0_v, p1_v, p_span) != class_list[doc_index]:
            error_count += 1
    print('the error rate is:', float(error_count) / len(test_set))


spam_test()
