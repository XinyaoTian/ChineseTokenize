import jieba
import pandas as pd
import numpy as np
import logging
import re
logging.basicConfig(level=logging.INFO)

# 中文去停用词的功能类 for python 3
class TokChinese:

    # 从 Github 仓库中读入停用词文本
    def __init__(self):
        # 载入停用词表
        self.df_stopwords = pd.read_csv("https://raw.githubusercontent.com/XinyaoTian/stopwords/master/stopwords.txt",
                         index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')#quoting=3全不引用
        
        # 用于记录词频统计的List
        self.count_list = []

    # 输入 string ；输出 切分好关键词的一个 list ; 若输入为None或切分时遇到了无法切分的情况，则返回一个空list []
    def cutDescription(self,description):
        segment = []
        if description is None:
            logging.info("Your input string is 'None'.")
            return []
        else:
            try:
                seg_list = jieba.lcut_for_search(description , HMM = True)
                for word in seg_list:
                    if len(word)>1 and word!='\n' and word!='.':
                        segment.append(word)
                return seg_list
            except:
                logging.info(str(description))
                logging.info("Can not cut the sentence using jieba.")
                return segment
                
    # 输入一个中文词语list，输出消除停用词的list
    def eliminateStopwords(self,word_list):
        df_words = pd.DataFrame({'segment':word_list})
        df_keywords = df_words[~df_words['segment'].isin(self.df_stopwords['stopword'])]
        return list(df_keywords['segment'])

    # 输入一个string 输出去停用词后的切分好的词语list[]
    def getTokenizedList(self , description):
        cut_list = self.cutDescription(description)
        token_list = self.eliminateStopwords(cut_list)
        return token_list
    
    # 输入一个string 输出去停用词后的切分好的并且去重的词语list[]
    def getAndDedupTokenizedList(self , description):
        cut_list = self.cutDescription(description)
        token_list = self.eliminateStopwords(cut_list)
        return self.dedup(token_list)
    
    # 输入一个string 输出去停用词后的切分好的英文词语list[]
    def getEnglishWordsList(self , description):
        english_list = []
        cut_list = self.cutDescription(description)
        token_list = self.eliminateStopwords(cut_list)
        for word in token_list:
            if re.match(r"[a-zA-z0-9]+",word) is not None:
                english_list.append(word)
            else:
                continue
        return english_list
    
    # 将输入字符串切分、去停用词后，剩下的所有词加入到self.count_list中,并返回当前去停用词得到的list
    def getTokenizedListAndAddToSelfList(self , description):
        cut_list = self.cutDescription(description)
        token_list = self.eliminateStopwords(cut_list)
        self.count_list.extend(token_list)
        return token_list
    
    # 统计self.count_list中的词频,并返回DF
    def countNumInSelfListWithDF(self):
        df_words=pd.DataFrame({'segment':self.count_list})
        df_keywords = df_words[~df_words['segment'].isin(self.df_stopwords['stopword'])]
        df_words_stat=df_keywords.groupby(by=['segment'])['segment'].agg({"count":np.size})
        df_words_stat=df_words_stat.reset_index().sort_values(by=["count"],ascending=False)
        return df_words_stat

    # 统计self.count_list中的词频，并返回Dict
    def countNumInSelfListWithDict(self):
        words_value_dict = {}
        for word in self.count_list:
            if words_value_dict.get(word) is not None:
                words_value_dict[word] += 1
            else:
                words_value_dict[word] = 1
        return words_value_dict
        
    
    # 重置self.count_dict
    def clearSelfList(self):
        self.count_list = []

    # 手动设置self.count_list中的词
    def setSelfList(self,count_list):
        self.count_list = count_list

    # 以list格式获取到self.count_list中的词
    def getSelfList(self):
        return self.count_list

    # 以pandas的DataFrame格式获取到self.count_list中的词
    def getSelfListInDF(self):
        return pd.DataFrame({'segment':self.count_list})
    
    # 传入一个list，输出将所有list拼接成的一个字符串
    def listToString(self,word_list):
        newString = ""
        for word in word_list:
            newString += str(word)
            newString += " "
        return newString
    
    # list中的元素去重
    # 输入 list ; 输出 去重后的list
    def dedup(self,word_list):
        word_set = set(word_list)
        return list(word_set)