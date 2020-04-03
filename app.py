import zipfile
import pandas as pd
from bs4 import BeautifulSoup

with zipfile.ZipFile("lot-parser.zip", "r") as zip:
    html_file_path = [item.filename for item in zip.filelist if item.filename.endswith('.html')]
    # print(len(html_file_path))
    for file in html_file_path:
        if file.startswith('__MACOSX'):
            continue
        print('\n','*'*5,file,'*'*5,'\n')
        htmlfile = zip.read(file).decode("utf-8")
        # bs1 = BeautifulSoup(htmlfile, "html.parser")
        # print(bs1,'\n\n\n')
        bs2 = BeautifulSoup(htmlfile, "html5lib")
        
        p1 = bs2.find('div')
        p11 = [item.strip().replace('  ', ' ') for item in p1.contents]
        print(p11)
        
        s1 = bs2.find('span')
        if s1:
            print(s1.contents)
        else:
            # print(bs2)
            p2 = p1.find_next()
            print(p2.contents)
            p3 = p2.find_next()
            print(p3.contents)
            continue
            # break

        s2 = s1.find_next()
        print(s2.contents)

        
        # break