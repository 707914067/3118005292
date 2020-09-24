import re
import sys
from util.simhash import SimHash

if __name__ == '__main__':

    try:
        with open(sys.argv[1], 'r', -1, 'utf-8') as f:  # 读取原文件
            s1 = f.read()
        with open(sys.argv[2], 'r', -1, 'utf-8') as f:  # 读取抄袭文件
            s2 = f.read()

        hash1 = SimHash(re.split(r'[，。！、：“”]', s1.replace('\n', '')))  # 分段后计算每段的哈希值与数字指纹
        hash2 = SimHash(re.split(r'[，。！、：“”]', s2.replace('\n', '')))

        with open(sys.argv[3], 'a', -1, 'utf-8') as f:
            f.write(sys.argv[1].split('/')[-1] + '与' + sys.argv[2].split('/')[-1])
            f.write('的相似度为' + str(hash1.similarity(hash2)) + '\n')  # 通过数字指纹算出相似值
    except IOError:
        print('Error: 没有找到文件或读取文件失败!')
