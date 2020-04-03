import zipfile
import pandas as pd
from bs4 import BeautifulSoup
import json

parse_result = {}

with zipfile.ZipFile("lot-parser.zip", "r") as zip:
    html_file_path = [item.filename for item in zip.filelist if item.filename.endswith('.html')]
    for file in html_file_path:
        if file.startswith('__MACOSX'):
            continue
        htmlfile = zip.read(file).decode("utf-8")
        bs_htmlfile = BeautifulSoup(htmlfile, "html5lib")
        
        div0_htmlfile = bs_htmlfile.find('div')
        extracted_data = list(map(lambda x:x.strip(), div0_htmlfile.contents[0].split("\n")))

        Artist = extracted_data[0]
        ArtName = extracted_data[1]
        About = ' '.join(extracted_data[2:])
        
        print('Artist: ', Artist)
        print('ArtName: ', ArtName)
        print('About: ', About)
        
        span0_htmlfile = bs_htmlfile.find('span')
        if span0_htmlfile:
            span1_htmlfile = span0_htmlfile.find_next()
            Price = ' '.join([span0_htmlfile.contents[0], span1_htmlfile.contents[0]])
            print('Price: ',Price)
        else:
            div1_htmlfile = div0_htmlfile.find_next()
            print(div1_htmlfile.contents)

            div2_htmlfile = div1_htmlfile.find_next()
            print(div2_htmlfile.contents)

            # Price = ' '.join([span1_htmlfile.contents[0], span0_htmlfile.contents[0]])
            Price = div2_htmlfile.contents[0]
            print('Price: ',Price)
            # break
            continue

        # Save to dict
        # parse_result.update({'Artist':Artist,'ArtName':ArtName, 'About':About, 'Price':Price})
        parse_result[Artist] = {'ArtName':ArtName, 'About':About, 'Price':Price}

# print(parse_result)


with open('parsed_html.json', 'w') as fp:
    json.dump(parse_result, fp)