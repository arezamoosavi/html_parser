import zipfile
import pandas as pd
from bs4 import BeautifulSoup
import json

parse_result = {'Name':[],'Art':[], 'About':[], 'Price':[]}

with zipfile.ZipFile("lot-parser.zip", "r") as zip:
    html_file_path = [item.filename for item in zip.filelist if item.filename.endswith('.html')]
    # print(len(html_file_path))
    for file in html_file_path:
        if file.startswith('__MACOSX'):
            continue
        print('\n','*'*5,file,'*'*5,'\n')
        htmlfile = zip.read(file).decode("utf-8")
        # bs1 = BeautifulSoup(htmlfile, "html.parser")
        bs2 = BeautifulSoup(htmlfile, "html5lib")
        
        p1 = bs2.find('div')
        p11 = [item.strip().replace('  ', ' ') for item in p1.contents]
        
        p21 = list(map(lambda x:x.strip(), p11[0].split("\n")))
        Artist = p21[0]
        ArtName = p21[1]
        About = ' '.join(p21[2:])
        
        print('Artist: ', Artist)
        print('ArtName: ', ArtName)
        print('About: ', About)
        
        s1 = bs2.find('span')
        if s1:
            s2 = s1.find_next()
            Price = ' '.join([s1.contents[0], s2.contents[0]])
            print('Price: ',Price)
        else:
            s1 = p1.find_next()
            print(s1.contents)

            s2 = s1.find_next()
            print(s2.contents)

            # Price = ' '.join([s2.contents[0], s1.contents[0]])
            Price = s2.contents[0]
            print('Price: ',Price)
            # break
            continue

        # Save to dict
        # break
    
    """
    with open('parsed_html.json', 'w') as fp:
        json.dump(parse_result, fp)"""