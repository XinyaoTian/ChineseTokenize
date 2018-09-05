自己编写的中文字符串切分、去停用词库(基于jieba)
Contact Me By Email: xinyaotian@yeah.net

Or By Github : https://github.com/XinyaoTian

导入TokChinese库中的TokChinese功能类

# 导入库中的TokChinese类
from TokChinese import TokChinese
getTokenizedList(string)
Input type : string
output type : list
输入一个string,输出切分、去停用词后词语list[]


tc = TokChinese()
stringA = "今天晚上我们去吃披萨吧！晚上吃披萨吧！"
?
# 使用getTokenizedList()
word_list = tc.getTokenizedList(stringA)
print(word_list)
print(type(word_list))
['晚上', '吃', '披萨', '晚上', '吃', '披萨']
<class 'list'>
getAndDedupTokenizedList(string)
Input type : string
output type : list
输入一个string,输出切分、去停用词、去重后词语list[]


tc = TokChinese()
stringA = "今天晚上我们去吃披萨吧！晚上吃披萨吧！"
?
# 使用 getAndDedupTokenizedList()
word_list = tc.getAndDedupTokenizedList(stringA)
print(word_list)
print(type(word_list))
['晚上', '吃', '披萨']
<class 'list'>
getEnglishWordsList(string)
Input type : string
output type : list
输入一个string,输出仅由“英文”构成的词语list[]


tc = TokChinese()
stringA = "Good morning!今天天气真不错。"
?
# 使用getEnglishWordsList()
word_list = tc.getEnglishWordsList(stringA)
print(word_list)
print(type(word_list))
['Good', 'morning']
<class 'list'>
getTokenizedListAndAddToSelfList(string)
Input type : string
output type : list
输入一个string,输出切分、去停用词后词语list[],并将这些切分好的词加入TokChinese类的一个list中

countNumInSelfListWithDict()
output type : dict
【!】 注意，使用这个函数之前需要先使用 getTokenizedListAndAddToSelfList()

返回一个dict，以词语为key、出现次数为value。生成本dict的来源是TokChinese类中的一个私有变量list,

使用getTokenizedListAndAddToSelfList(string)把词语添加进入TokChinese类中私有变量list


tc = TokChinese()
stringA = "Good morning!今天天气真不错。昨天的天气也很不错"
?
# 使用getTokenizedListAndAddToSelfList()
word_list = tc.getTokenizedListAndAddToSelfList(stringA)
print(word_list)
print(type(word_list))
?
# 在使用了 getTokenizedListAndAddToSelfList() 后，使用 countNumInSelfListWithDict() 统计词频
count_dict = tc.countNumInSelfListWithDict()
print(count_dict)
print(type(count_dict))
['Good', ' ', 'morning', '天天', '天气', '今天天气', '真不', '不错', '真不错', '昨天', '天气', '不错']
<class 'list'>
{'Good': 1, '真不错': 1, '天气': 2, ' ': 1, '今天天气': 1, '真不': 1, 'morning': 1, '不错': 2, '天天': 1, '昨天': 1}
<class 'dict'>
getSelfList()
output type : list 返回一个存储在类中的list
clearSelfList()
output type : list 重置存储在类中的list

tc = TokChinese()
stringA = "Good morning!今天天气真不错。昨天的天气也很不错"
?
# 切分string并将切分次加入类中的list
word_list = tc.getTokenizedListAndAddToSelfList(stringA)
?
# 查看类中的list
selfList = tc.getSelfList()
print("Before cleaning:" + str(selfList))
?
# 清空self.list
tc.clearSelfList()
?
# 再次查看类中的list
selfList = tc.getSelfList()
print("After cleaning:" + str(selfList))
Before cleaning:['Good', ' ', 'morning', '天天', '天气', '今天天气', '真不', '不错', '真不错', '昨天', '天气', '不错']
After cleaning:[]
感谢您的使用
The End