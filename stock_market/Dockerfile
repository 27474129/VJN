FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN mkdir /stock_market/
COPY . /stock_market/
WORKDIR /stock_market/
RUN cd /stock_market/


RUN pip3 install -r requirements.txt

CMD ["python3", "execute_stock_market.py"]
