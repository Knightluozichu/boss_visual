import jieba  # 分词
import matplotlib
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
from pymysql import *
import json
matplotlib.use('Agg')  # 使用非交互式后端
import matplotlib.pyplot as plt


# wordCloud

# 所有词
def get_img(field, targetImgSrc, resImgSrc):
    con = connect(host='localhost', user='root', password='123456', database='boss', port=3306, charset='utf8mb4')
    cursor = con.cursor()
    sql = f"select {field} from jobinfo"
    cursor.execute(sql)
    data = cursor.fetchall()
    text = ''
    if field == 'companyTags':
        for i, item in enumerate(data):
            if item[0] != '无':
                tags = json.loads(item[0])
                # print(tags)
                for j in tags:
                    text = text + j
    else:
        for i, item in enumerate(data):
            text += item[0]

    cursor.close()
    con.close()

    # 分词
    cut = jieba.cut(text)
    string = ' '.join(cut)
    # print(string)

    # 图片
    img = Image.open(targetImgSrc)  # 打开遮罩图片
    img_arr = np.array(img)  # 将图片转化为列表
    wc = WordCloud(
        background_color='white',
        mask=img_arr,
        font_path='STHUPO.TTF'
    )
    wc.generate_from_text(string)

    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')  # 不显示坐标轴

    # 显示生成的词语图片
    # plt.show()

    # 输入词语图片到文件
    plt.savefig(resImgSrc, dpi=500)


def get_addressCompanyTags_img(targetImgSrc, resImgSrc, addrress):
    con = connect(host='localhost', user='root', password='123456', database='boss', port=3306, charset='utf8mb4')
    cursor = con.cursor()
    sql = f"select companyTags from jobinfo where address = '{addrress}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    text = ''
    for i, item in enumerate(data):
        if item[0] != '无':
            tags = json.loads(item[0])
            # print(tags)
            for j in tags:
                text = text + j
    cursor.close()
    con.close()

    # 分词
    cut = jieba.cut(text)
    string = ' '.join(cut)
    # print(string)

    # 图片
    img = Image.open(targetImgSrc)  # 打开遮罩图片
    img_arr = np.array(img)  # 将图片转化为列表
    wc = WordCloud(
        background_color='white',
        mask=img_arr,
        font_path='STHUPO.TTF'
    )
    wc.generate_from_text(string)

    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')  # 不显示坐标轴

    # 显示生成的词语图片
    # plt.show()

    # 输入词语图片到文件
    plt.savefig(resImgSrc, dpi=500)



get_img('companyTitle',r'.\static\2.jpg',r'.\static\companyTitle.jpg')
get_img('companyTags', r'.\static\2.jpg', r'.\static\companyTags.jpg')

# import os
#
# print(os.path.exists('static/2.jpg'))  # 检查文件是否存在
# print(os.getcwd())  # 打印当前工作目录
