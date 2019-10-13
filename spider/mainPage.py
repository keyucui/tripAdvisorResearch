#encoding=utf-8
import re
import urllib.request
import time


def hotelOfTexas(url):
    try:

        headers = ("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        req = urllib.request.Request(url)
        # req.add_header()
        data = urllib.request.urlopen(req).read().decode('utf-8')  # 爬取网页的内容
        # print(data)
        pat_hotel_url = '''ui_column is-8 main_col.+class="listing_title"><a target="_blank" href=".+html" id='''
        # pat_all = '''<span class="textSpan">\n<a href="/.+.html" target="_blank" title=".+">\n<span class=".+">.+</span>\n</a>\n<em>\n\d+亮\d+回复</em>'''
        pat_hotel_url = re.compile(pat_hotel_url)
        results = pat_hotel_url.findall(data)
        return results
        # return 0
    except Exception as e:
        print('连接异常-->' + str(e))
        return -1



if __name__=='__main__':
    t = time.time()
    url = 'https://www.tripadvisor.cn/Hotels-g28964-Texas-Hotels.html'
    results = hotelOfTexas(url)
    print(len(results))
    for item in results:
        print(item)
    print('\n总共花费了%f秒'%(time.time() - t))
    time.sleep(10)
