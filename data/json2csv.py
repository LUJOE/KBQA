import json
import pandas as pd
# data = json.load(open('./qa_corpus.json/qa_corpus.json','r',encoding = 'utf-8'))#数据量太大，无法读取
# df = pd.DataFrame(data["answer"])
JSonfile = open("./qa_corpus.json/qa_corpus.json", 'r', encoding='utf-8')
papers = []
for line in JSonfile.readlines():
    dic = json.loads(line)
    df_question = str(dic["question"]).replace('\n','')
    df_answer = str(dic["answers"]).replace('\n','')
    df_category = str(dic["category"])
    if df_category in category_list and len(paperspapers) <= 1000:
        df_category_index = str(category_list.index(df_category))
        Textfile = open("./qa_corpus.json/one_hop_transE_1000.txt", 'a+', encoding='utf-8')
        Textfile.write(df_question + '\t' + df_category + '\t' + df_answer + '\n')
        papers.append(dic)
    else:
        df_category_index = str(len(category_list))
print(len(papers))



# print(df.head())

# from pandas.io.json import json_normalize
# import json
#
# with open('json_file.json') as data_file:
#     d= json.load(data_file)
#
# df = json_normalize(d, 'result').assign(**d['status'])
# print (df)