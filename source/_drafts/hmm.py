# -*- coding: utf-8 -*-
#
# @author hztancong
#


trans_prob = {"周杰":0.9,
              "周姐":0.1,
              "周洁":0.3,
              "杰伦":0.8,
              "结论":0.7
              }



pi = {
    "周":0.5,
    "粥":0.3,
    "杰":0.5,
    "姐":0.4,
    "节":0.2,
    "结":0.3,
    "轮":0.1,
    "伦":0.5,
    "论":0.5,
}

emit_prob = {
    "zhou周":0.5,
    "zhou粥":0.1,
    "jie姐":0.1,
    "jie节":0.1,
    "jie结":0.2,
    "lun轮":0.1,
    "lun伦":0.3,
    "lun论":0.1,
}

def viterbi(word_list, T, word2idx):
    """
    维特比算法求解最大路径问题
    :param word_list:
    :param s_num:
    :param word2idx:
    :return:
    """
    delta = [[0 for _ in range(s_num)] for _ in range(len(word_list))]

    delta = np.zeros((T, self.n))
    psi = np.zeros((T, self.n))

    # print delta
    words = word_list[0]
    for w in words:
        delta[0][word2idx[w]] = pi[w]

    for idx in range(1, len(word_list)):
        words = word_list[idx]
        for i in range(len(words)):
            max_value = 0
            pre_words = word_list[idx-1]
            for j in range(len(pre_words)):
                tmp_key = pre_words[j]+words[i]
                # print tmp_key
                if tmp_key in trans_prob:
                    prob = trans_prob[tmp_key]
                else:
                    prob = 0
                tmp_value = delta[idx-1][word2idx[pre_words[j]]] * prob
                if max_value < tmp_value:
                    max_value = tmp_value

            delta[idx][word2idx[words[i]]] = max_value

    print delta
    # 终止

    word_len = len(word_list)
    prob = 0
    path = [0 for _ in range(word_len)]
    path[word_len - 1] = 1
    n = word_len(pi)
    for i in range(n):
        if prob < delta[word_len - 1][i]:
            prob = delta[word_len - 1][i]
            path[word_len - 1] = i

    # 最优路径回溯
    for t in range(word_len - 2, -1, -1):
        path[t] = psi[t+1][path[t+1]]

    return path, prob, delta, psi

if __name__ == "__main__":
    word_list = [["周", "粥"], ["杰", "姐", "节", "结"], ["轮", "伦", "论"]]
    words = set()
    for wl in word_list:
        for w in wl:
            words.add(w)

    word2idx = dict()
    idx = 0
    for w in words:
        word2idx[w] = idx
        # print w, idx
        idx += 1
    # print trans_prob
    viterbi(word_list, len(words), word2idx)


