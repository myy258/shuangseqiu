import sys
import pandas as pd
import requests
from lxml import etree

def get_url(url):       #请求url的方法，返回html
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    response = requests.get(url,headers=headers)        #获取请求的返回数据
    response.encoding = 'utf-8'         #定义编码，不然中文输出会乱码；
    if response.status_code == 200:     #如果请求成功，则返回；
        return response.text
    return None

result_data = []
for q in range(1,125):      #for循环，一共124页；
    url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % (q)   #定义请求的链接
    html = get_url(url)         #请求url获取返回代码
    xpath_html = etree.HTML(html)       #xpath初始化html代码

    dates = xpath_html.xpath('//table[@class="wqhgt"]//tr//td[1]//text()')      #获取开奖日期
    result = xpath_html.xpath('//table[@class="wqhgt"]//tr//em//text()')        #获取上色球号
    issues = xpath_html.xpath('//table[@class="wqhgt"]//tr//td[2]//text()')     #获取期号
    # print(result)       #输出所有双色球的列
    # print(len(result)//7)    #输出有几组双色球
    # print(dates)
    # print(issues)
    sta = 0
    end = 7
    for n in range(len(result)//7):     #双色球7个号一组，
        aa = result[sta:end]
        bb = [int(x) for x in aa]
        result_data.append(bb)
        sta = sta + 7
        end = end + 7
df = pd.DataFrame(result_data,columns = ['red1','red2','red3','red4','red5','red6','blue'])
listr = [[1,2,20,22,29,31,12],[2,5,11,15,19,25,6],[8,9,15,16,21,22,3],[3,9,18,20,31,32,6],[6,10,17,18,25,30,9]]


def element_for2_percent(data):
    element_for2 = []
    for i in range(len(data)):
        element_for2.append(data[i][0:2])
        
    map = {}
    for item in element_for2:
            s = str(item)
            if s in map.keys():
                map[s] = map[s] + 1
            else:
                map[s] = 1 
    df2 = pd.DataFrame.from_dict(map, orient='index',columns=['count'])
    df2 = df2.reset_index().rename(columns = {'index':'id'})
    df2['percent'] = round(df2['count'] / df2['count'].sum(),3)
    df2 = df2.sort_index(by=['count'],ascending=False)
    return df2
for2 = element_for2_percent(result_data)

def element_for3_percent(data):
    element_for3 = []
    for i in range(len(data)):
        element_for3.append(data[i][0:3])
        
    map = {}
    for item in element_for3:
            s = str(item)
            if s in map.keys():
                map[s] = map[s] + 1
            else:
                map[s] = 1 
    df2 = pd.DataFrame.from_dict(map, orient='index',columns=['count'])
    df2 = df2.reset_index().rename(columns = {'index':'id'})
    df2['percent'] = round(df2['count'] / df2['count'].sum(),3)
    df2 = df2.sort_index(by=['count'],ascending=False)
    return df2
for3 = element_for3_percent(result_data)

def element_for4_percent(data):
    element_for4 = []
    for i in range(len(data)):
        element_for4.append(data[i][0:4])
        
    map = {}
    for item in element_for4:
            s = str(item)
            if s in map.keys():
                map[s] = map[s] + 1
            else:
                map[s] = 1 
    df2 = pd.DataFrame.from_dict(map, orient='index',columns=['count'])
    df2 = df2.reset_index().rename(columns = {'index':'id'})
    df2['percent'] = round(df2['count'] / df2['count'].sum(),3)
    df2 = df2.sort_index(by=['count'],ascending=False)
    return df2
for4 = element_for4_percent(result_data)

def element_for5_percent(data):
    element_for5 = []
    for i in range(len(data)):
        element_for5.append(data[i][0:5])
        
    map = {}
    for item in element_for5:
            s = str(item)
            if s in map.keys():
                map[s] = map[s] + 1
            else:
                map[s] = 1 
    df2 = pd.DataFrame.from_dict(map, orient='index',columns=['count'])
    df2 = df2.reset_index().rename(columns = {'index':'id'})
    df2['percent'] = round(df2['count'] / df2['count'].sum(),3)
    df2 = df2.sort_index(by=['count'],ascending=False)
    return df2
for5 = element_for5_percent(result_data)

c = for5.append(for4)
c1 = c.append(for3)
c2 = c1.append(for2)

sss = [[1, 2, 20, 22, 29],[2, 8, 11, 15, 19],[8, 9, 15, 16, 21],[3, 9, 18, 20, 31],[6, 10, 17, 18, 25]]
sss1 =  ['[3, 9, 18, 20]']
for s in sss1:
    if s in (c2['id'].values.tolist()):
        print('have')

