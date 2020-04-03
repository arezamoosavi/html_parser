FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY lot-parser.zip .

CMD python app.py