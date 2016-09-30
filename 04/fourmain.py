__author__ = 'williamscullion'

import urllib.request as req


nothings = [12345]


for i in range(401):

    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(str(nothings[i]))
    web_page = req.urlopen(url)
    web_page_info = web_page.read()
    web_page_info_uni = web_page_info.decode('utf-8')

    a = [int(s) for s in web_page_info_uni.split() if s.isdigit()]
    print(i, ": ", a, web_page_info_uni)
    if not a:
        a = [nothings[i] / 2]
        print("Divided by two!")
    nothings.append(a[0])



