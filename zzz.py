import tkinter
import tkinter.font
from tkinter.font import Font
import requests
from pyquery import PyQuery as pq
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# 这里我使用了代理  你可以去掉这个代理IP 我是为了后面大规模爬取做准备的
proxies = {
    'https': '218.75.69.50:39590'
}

# 请求网页 获取源码
def start_request(url):
    r = requests.get(url, headers=headers)
    # 这个网站页面使用的是utf-8编码 这里进行编码转换
    r.encoding = 'utf-8'
    html = r.text
    return html


def parse(text):
    doc = pq(text)
    # 锁定页面中的img标签
    images = doc('div.wallpaperList div.wallpaperBg img').items()
    x = 0
    for image in images:
        # 获取每一张图片的链接
        img_url = image.attr('src')
        print(img_url)
        # 获得每张图片的二进制内容
        img = requests.get('https://www.wallpapermaiden.com/'+img_url, headers=headers).content
        # 定义要存储图片的路劲
        path = "C:\\Users\\86132\\Desktop\\images\\images" + str(x) + ".jpeg"
        # 将图片写入指定的目录 写入文件用"wb"
        with open(path, 'wb') as f:
            f.write(img)
            time.sleep(1)
            bdl = ("正在下载第{}张图片").format(x)
            l1.insert(tkinter.END, bdl)
            print(bdl)
            x += 1
    print("写入完成")
    l1.insert(tkinter.END, "已经写入本页面所有图片")


zqy = tkinter.Tk()
zqy.title('大项目')
zqy.geometry("1200x800+200+50")
zqy.resizable(0, 0)

t = True
f = False
i = ["3d", "abstract", "animal", "anime", "cars", "city", "dark", "fantasy", "flowers", 
    "food", "games", "girls", "landscape", "men","movies", "nature", "other", "sci-fi", "space", "sports", "technology", "vehicle"]

oo = ["3d", "abstract", "animal", "anime", "cars", "city", "dark", "fantasy", "flowers", 
    "food", "games", "girls", "landscape", "men","movies", "nature", "other", "sci-fi", "space", "sports", "technology", "vehicle"]    

n = ["3D", "抽象", "动物", "日漫", "汽车", "城市", "黑暗", "幻想", "花卉", "餐饮", "游戏", 
    "女生", "景观", "男装", "电影", "性质", "其他", "科幻", "空间", "体育", "技术", "车辆"]


def updata():
    print(r.get())
    


top = tkinter.Frame(zqy, bg='black', width=100, height=600)

r = tkinter.IntVar()
fw = Font(family="微软雅黑", size=13)

i[0] = tkinter.Radiobutton(top, text=n[0], value=1, variable=r, command=updata, bg="pink", font=fw)
i[0].pack()
i[1] = tkinter.Radiobutton(top, text=n[1], value=2, variable=r, command=updata, bg="pink", font=fw)
i[1].pack()
i[2] = tkinter.Radiobutton(top, text=n[2], value=3, variable=r, command=updata, bg="pink", font=fw)
i[2].pack()
i[3] = tkinter.Radiobutton(top, text=n[3], value=4, variable=r, command=updata, bg="pink", font=fw)
i[3].pack()
i[4] = tkinter.Radiobutton(top, text=n[4], value=5, variable=r, command=updata, bg="pink", font=fw)
i[4].pack()
i[5] = tkinter.Radiobutton(top, text=n[5], value=6, variable=r, command=updata, bg="pink", font=fw)
i[5].pack()
i[6] = tkinter.Radiobutton(top, text=n[6], value=7, variable=r, command=updata, bg="pink", font=fw)
i[6].pack()
i[7] = tkinter.Radiobutton(top, text=n[7], value=8, variable=r, command=updata, bg="pink", font=fw)
i[7].pack()
i[8] = tkinter.Radiobutton(top, text=n[8], value=9, variable=r, command=updata, bg="pink", font=fw)
i[8].pack()
i[9] = tkinter.Radiobutton(top, text=n[9], value=10, variable=r, command=updata, bg="pink", font=fw)
i[9].pack()
i[10] = tkinter.Radiobutton(top, text=n[10], value=11, variable=r, command=updata, bg="pink", font=fw)
i[10].pack()
i[11] = tkinter.Radiobutton(top, text=n[11], value=12, variable=r, command=updata, bg="pink", font=fw)
i[11].pack()
i[12] = tkinter.Radiobutton(top, text=n[12], value=13, variable=r, command=updata, bg="pink", font=fw)
i[12].pack()
i[13] = tkinter.Radiobutton(top, text=n[13], value=14, variable=r, command=updata, bg="pink", font=fw)
i[13].pack()
i[14] = tkinter.Radiobutton(top, text=n[14], value=15, variable=r, command=updata, bg="pink", font=fw)
i[14].pack()
i[15] = tkinter.Radiobutton(top, text=n[15], value=16, variable=r, command=updata, bg="pink", font=fw)
i[15].pack()
i[16] = tkinter.Radiobutton(top, text=n[16], value=17, variable=r, command=updata, bg="pink", font=fw)
i[16].pack()
i[17] = tkinter.Radiobutton(top, text=n[17], value=18, variable=r, command=updata, bg="pink", font=fw)
i[17].pack()
i[18] = tkinter.Radiobutton(top, text=n[18], value=19, variable=r, command=updata, bg="pink", font=fw)
i[18].pack()
i[19] = tkinter.Radiobutton(top, text=n[19], value=20, variable=r, command=updata, bg="pink", font=fw)
i[19].pack()
i[20] = tkinter.Radiobutton(top, text=n[20], value=21, variable=r, command=updata, bg="pink", font=fw)
i[20].pack()
i[21] = tkinter.Radiobutton(top, text=n[21], value=22, variable=r, command=updata, bg="pink", font=fw)
i[21].pack()

ft = Font(family="FangSong", size=90)
fa = Font(family="微软雅黑", size=18)
t1 = tkinter.Label(zqy, font=ft, text="s\np\ni\nd\ne\nr")
b1 = tkinter.Button(zqy, text="START\nstart\n开始\n始める", font=fw, bg="black", foreground='white', )
l1 = tkinter.Listbox(zqy, bg="black", foreground='green', height=700, width=500, justify="left", font=fa)
l1.place(x=700, y=0, width=490, height=800)


yscrollbar = tkinter.Scrollbar(l1, command=l1.yview)
yscrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
l1.config(yscrollcommand=yscrollbar.set)

def main(ebent):
    m = r.get()
    n = m - 1
    url_last = oo[n]
    print(url_last)
    url = "https://www.wallpapermaiden.com/category/"+url_last
    text = start_request(url)
    parse(text)


b1.bind("<Button-1>", main)

t1.pack(side='left')
top.pack(side="left")
b1.pack(side="left", padx=100, ipadx=100)

zqy.mainloop()
