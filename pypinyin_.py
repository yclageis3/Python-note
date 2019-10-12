# 拼音库
import pypinyin

# python 内置函数
from functools import reduce

"""
Python 第三方库 pypinyin 的简单使用
"""

str_a = r'你好中国!'


""" 返回结果:二维列表 """
style_1 = pypinyin.pinyin(str_a)
print(style_1)  # [['nǐ'], ['hǎo'], ['zhōng'], ['guó'], ['!']]  默认样式:有音调

style_2 = pypinyin.pinyin(str_a, style=pypinyin.NORMAL)  
print(style_2)  # [['ni'], ['hao'], ['zhong'], ['guo'], ['!']]  常用 不带音调

style_3 = pypinyin.pinyin(str_a, style=pypinyin.STYLE_TONE2)
print(style_3)  # [['ni3'], ['ha3o'], ['zho1ng'], ['guo2'], ['!']]  供外国友人纠正发音的写法 

style_4 = pypinyin.pinyin(str_a, style=pypinyin.FINALS_TONE3)  
print(style_4)  # [['i3'], ['ao3'], ['ong1'], ['uo2'], ['!']]  没看懂.....

""" 其他的就不测试了, 常用的就是第二种 """

########################################################################

""" 将返回的二维列表转为可用的str """

# 1、中规中矩的办法 写个函数 for循环遍历追加
def to_str(pinyin_list: list) -> str:
    pinyin = ''

    for item in pinyin_list:
        pinyin += item[0]

    return pinyin

new_str = to_str(style_2)
print(new_str)  # nihaozhongguo!

# 2、骚操作 使用内置函数 reduce
"""
reduces 配合 lambda 函数, 将目标列表作用于 指定lambda函数, x, y 可看作 前一个元素和后一个元素
"""
pinyin_list = reduce(lambda x, y: x + y, style_2)  # 第一次使用, 二维合并为一维 ['ni', 'hao', 'zhong', 'guo', '!']
new_str = reduce(lambda x, y: x + y, pinyin_list)  # 第二次使用, 合并为正常可用的str  nihaozhongguo!
print(new_str)

