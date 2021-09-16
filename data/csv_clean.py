# import csv
# csv_reader = csv.reader(open("./original.csv"))
# for line in csv_reader:
#     print(line)
import re

def get_features():
    papers = []
    law_list = []  # 使用了什么法律
    crime_list = []  # 判决了什么罪行
    law_line_str = ''
    crime_line_str = ''
    with open('test_case.txt', 'r', encoding='UTF-8') as text_file:
        lines = text_file.readlines()    # 接收数据
        for line in lines:     # 遍历数据
            title = line.split('\t')[0] #标题
            type = line.split('\t')[2]  #类型
            type_small = line.split('\t')[4]  #具体类型
            person = line.split('\t')[17]  #当事人
            des = line.split('\t')[19] #庭审程序说明
            des_small = line.split('\t')[21]  #庭审过程描述
            result = line.split('\t')[27]  #庭审结果
            result_law = line.split('\t')[28]  #判决结果
            if len(result_law)>=5 and len(papers) <= 1000:
                # law_name = result_law.split('《')[1].split('》')[0]
                law_line = re.findall(r"《(.+?)》",result_law)
                crime_line = re.findall(r"犯(.+?)罪", result_law)

                for law_name in law_line:
                    law_line_str = law_line_str + law_name +' '
                    if law_name not in law_list :
                        law_list.append(law_name)
                for crime_name in crime_line:
                    crime_line_str = crime_line_str + crime_name + ' '
                    if crime_name not in crime_list:
                        crime_list.append(crime_name)

                with open(train_path, 'a+', encoding='UTF-8') as train_file:
                    print ('des: ',des)
                    print('law_line_str: ', law_line_str)
                    print('crime_line_str: ', crime_line_str)
                    train_file.write(des + '\t' + law_line_str + '\t' + crime_line_str + '\t')
                papers.append(line)

    print('law_list: ',law_list)
    with open(law_path, 'a+', encoding='UTF-8') as law_file:
        for law_name in law_list:
         law_file.write(law_name + '\n')
    with open(crime_path, 'a+', encoding='UTF-8') as crime_file:
        for crime_name in crime_list:
         crime_file.write(crime_name + '\n')

    print(len(papers))

if __name__ == '__main__':

    train_path = 'train_law.txt'
    test_path = 'test_law.txt'
    law_path = 'law.txt'
    crime_path = 'crime.txt'
    get_features()