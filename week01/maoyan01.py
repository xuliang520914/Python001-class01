"""
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
url = 'https://maoyan.com/films?showType=3'
cookie = 'uuid_n_v=v1; uuid=165B23F0B6E111EA9B3075693A212BAFE4BE70CB6B8F49A09C663184ECBA4F6B; _csrf=8ca27885cc7988243e1a912bc0b8b3343a5b17b36201685389210d0c4f57095a; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=172eb7e9fb273-0f6f77dbf11517-f7d123e-1fa400-172eb7e9fb3c8; _lxsdk=165B23F0B6E111EA9B3075693A212BAFE4BE70CB6B8F49A09C663184ECBA4F6B; mojo-uuid=c0ebaf63df5f6e71c426b133df429079; mojo-session-id={"id":"ddd3c048566b8b2d411a4fdaa643dc5f","time":1593088844322}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593088844,1593089550; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593089854; __mta=251551289.1593088843792.1593089847689.1593089854611.7; mojo-trace-id=11; _lxsdk_s=172eb7e9fb4-3b1-1f5-167%7C%7C18'

header = {'user-agent': user_agent, 'Cookie': cookie}

# 获取到内容
response = requests.get(url, headers=header)
# print(response.status_code, response.text)


def get_top_ten(html):
    ba_info = bs(html.text, 'html.parser')
    movie_list = []

    # 获取前10个电影名称，类型，上映时间
    for idx, tags in enumerate(ba_info.find_all('div', attrs={'class': 'movie-item-hover'})):
        name = tags.find(class_='name').text
        genre = tags.find_all(class_='movie-hover-title')[1].text[5:].strip()
        release_time = tags.find_all(class_='movie-hover-title')[3].text[7:].strip()
        movie_list.append((name, genre.strip(), release_time.strip()))
        if idx == 9:
            break

    return movie_list


movies = get_top_ten(response)
print(movies)
movie = pandas.DataFrame(movies)
movie.to_csv('movie.csv', encoding='utf-8')
