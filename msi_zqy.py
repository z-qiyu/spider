from selenium import webdriver
import requests
import json

print('请输入关键词（such as---歌名,歌手）\n请输入:')
s = input()
url = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=" + s
print(url)
driver = webdriver.PhantomJS()
driver.get(url)
driver.implicitly_wait(5)
xpath = driver.find_elements_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li/div/div[2]/span/a')
for xp in xpath:
    url = xp.get_attribute('href')
    name = xp.get_attribute('title')
    data = {'mid': url}
    print('正在下载---------------' + name)
    #借用第三方解析
    response = requests.post('http://www.douqq.com/qqmusic/qqapi.php', data=data).json()
    resJson = json.loads(response)
    music = requests.get(resJson['m4a']).content
    f = open('C:\\Users\\86132\\Desktop\\musics\\' + name + '.mp3', 'wb')
    print(' ---------------下载完毕')
    f.write(music)
    f.close()
print('已经完成下载！！！！！')
