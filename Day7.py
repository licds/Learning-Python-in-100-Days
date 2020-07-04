"""
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
"""
"""
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
"""
"""
set1 = {1, 2, 3, 3, 3, 2}
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set1)
print(set2)
print(set3)
print(set1 & set2) #middle
print(set1 | set2) #union
print(set2 - set1) #difference
print(set1 ^ set2) #non middle
print(set2 <= set1) #subset
print(set3 <= set1) #subset
"""
"""
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
"""
#practice 1
"""
import os
import time
def main():
    words = "Hello, world!"
    while True:
        print(words[0])
        time.sleep(0.2)
        words=words[1:] + words[0]
if __name__ == "__main__":
    main()
"""
"""
import os
import time

def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
"""
#practice 2
"""
import random
def codegenerator(code_length=4):
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    code = ""
    for i in range(code_length):
        index=random.randint(0,len(characters)-1)
        code+=characters[index]
    return code
"""
#practice 3
'''
def get_suffix(filename):
    index = filename.find(".")
    newIndex = index+1
    if len(filename[newIndex:]) == len(filename):
        return ""
    else:
        return filename[newIndex:]
'''
#practice 6
def main():
    numOfRows = int(input("Enter the number of rows: "))
    yh = [[]] * numOfRows 
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# # sorted函数返回列表排序后的拷贝不会修改传入的列表
# # 函数的设计就应该像sorted函数一样尽可能不产生副作用
# list3 = sorted(list1, reverse=True)
# # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# # 给列表对象发出排序消息直接在列表对象上进行排序
# list1.sort(reverse=True)
# print(list1)
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a


# def main():
#     for val in fib(20):
#         print(val)


# if __name__ == '__main__':
#     main()
# scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# print(scores)
# # 创建字典的构造器语法
# items1 = dict(one=1, two=2, three=3, four=4)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1, 10)}
# print(items1, items2, items3)
# # 通过键可以获取字典中对应的值
# print(scores['骆昊'])
# print(scores['狄仁杰'])
# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('基' if person else '非', end='')


# if __name__ == '__main__':
#     main()