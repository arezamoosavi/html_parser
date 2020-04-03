# HTML Parser

> This code will parse html pages from zip file into json file.

----
## usage

    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt
    python app.py
### With docker
    
    docker build -t artparser_app .
    docker run -it --rm artparser_app
---
## Sample result

```json
"Artist":
["ArtName", "About", "Price"]
```