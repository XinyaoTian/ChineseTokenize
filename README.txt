�Լ���д�������ַ����з֡�ȥͣ�ôʿ�(����jieba)
Contact Me By Email: xinyaotian@yeah.net

Or By Github : https://github.com/XinyaoTian

����TokChinese���е�TokChinese������

# ������е�TokChinese��
from TokChinese import TokChinese
getTokenizedList(string)
Input type : string
output type : list
����һ��string,����з֡�ȥͣ�ôʺ����list[]


tc = TokChinese()
stringA = "������������ȥ�������ɣ����ϳ������ɣ�"
?
# ʹ��getTokenizedList()
word_list = tc.getTokenizedList(stringA)
print(word_list)
print(type(word_list))
['����', '��', '����', '����', '��', '����']
<class 'list'>
getAndDedupTokenizedList(string)
Input type : string
output type : list
����һ��string,����з֡�ȥͣ�ôʡ�ȥ�غ����list[]


tc = TokChinese()
stringA = "������������ȥ�������ɣ����ϳ������ɣ�"
?
# ʹ�� getAndDedupTokenizedList()
word_list = tc.getAndDedupTokenizedList(stringA)
print(word_list)
print(type(word_list))
['����', '��', '����']
<class 'list'>
getEnglishWordsList(string)
Input type : string
output type : list
����һ��string,������ɡ�Ӣ�ġ����ɵĴ���list[]


tc = TokChinese()
stringA = "Good morning!���������治��"
?
# ʹ��getEnglishWordsList()
word_list = tc.getEnglishWordsList(stringA)
print(word_list)
print(type(word_list))
['Good', 'morning']
<class 'list'>
getTokenizedListAndAddToSelfList(string)
Input type : string
output type : list
����һ��string,����з֡�ȥͣ�ôʺ����list[],������Щ�зֺõĴʼ���TokChinese���һ��list��

countNumInSelfListWithDict()
output type : dict
��!�� ע�⣬ʹ���������֮ǰ��Ҫ��ʹ�� getTokenizedListAndAddToSelfList()

����һ��dict���Դ���Ϊkey�����ִ���Ϊvalue�����ɱ�dict����Դ��TokChinese���е�һ��˽�б���list,

ʹ��getTokenizedListAndAddToSelfList(string)�Ѵ�����ӽ���TokChinese����˽�б���list


tc = TokChinese()
stringA = "Good morning!���������治�����������Ҳ�ܲ���"
?
# ʹ��getTokenizedListAndAddToSelfList()
word_list = tc.getTokenizedListAndAddToSelfList(stringA)
print(word_list)
print(type(word_list))
?
# ��ʹ���� getTokenizedListAndAddToSelfList() ��ʹ�� countNumInSelfListWithDict() ͳ�ƴ�Ƶ
count_dict = tc.countNumInSelfListWithDict()
print(count_dict)
print(type(count_dict))
['Good', ' ', 'morning', '����', '����', '��������', '�治', '����', '�治��', '����', '����', '����']
<class 'list'>
{'Good': 1, '�治��': 1, '����': 2, ' ': 1, '��������': 1, '�治': 1, 'morning': 1, '����': 2, '����': 1, '����': 1}
<class 'dict'>
getSelfList()
output type : list ����һ���洢�����е�list
clearSelfList()
output type : list ���ô洢�����е�list

tc = TokChinese()
stringA = "Good morning!���������治�����������Ҳ�ܲ���"
?
# �з�string�����зִμ������е�list
word_list = tc.getTokenizedListAndAddToSelfList(stringA)
?
# �鿴���е�list
selfList = tc.getSelfList()
print("Before cleaning:" + str(selfList))
?
# ���self.list
tc.clearSelfList()
?
# �ٴβ鿴���е�list
selfList = tc.getSelfList()
print("After cleaning:" + str(selfList))
Before cleaning:['Good', ' ', 'morning', '����', '����', '��������', '�治', '����', '�治��', '����', '����', '����']
After cleaning:[]
��л����ʹ��
The End