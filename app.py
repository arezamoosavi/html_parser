import zipfile
from bs4 import BeautifulSoup
import json

parse_result = dict()
ArtistList = set()

with zipfile.ZipFile("lot-parser.zip", "r") as zip:
    html_file_path = [item.filename for item in zip.filelist if item.filename.endswith('.html')]
    for file in html_file_path:
        if file.startswith('__MACOSX'):
            continue
        htmlfile = zip.read(file).decode("utf-8")
        bs_htmlfile = BeautifulSoup(htmlfile, "html5lib")
        
        div0_htmlfile = bs_htmlfile.find('div')
        listContents = [item.strip() for item in div0_htmlfile.contents]
        extracted_data = list(map(lambda x:x.strip(), listContents[0].split("\n")))

        Artist = extracted_data[0]
        ArtName = extracted_data[1]
        About = ' '.join(extracted_data[2:])
        
        span0_htmlfile = bs_htmlfile.find('span')
        if span0_htmlfile:
            span1_htmlfile = span0_htmlfile.find_next()
            Price = ' '.join([span0_htmlfile.contents[0], span1_htmlfile.contents[0]])
        else:
            div1_htmlfile = div0_htmlfile.find_next()
            div2_htmlfile = div1_htmlfile.find_next()
            Price = div2_htmlfile.contents[0]

        if Artist in ArtistList:
            parse_result[Artist].append([ArtName, About, Price])
        else:
            parse_result[Artist] = [ArtName, About, Price]
            ArtistList.add(Artist)

with open('parsed_html.json', 'w') as fp:
    json.dump(parse_result, fp)