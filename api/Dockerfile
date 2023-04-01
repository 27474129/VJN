FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN mkdir /api/
COPY . /api/
WORKDIR /api/

RUN cd /api/

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "app:app", "--reload", "--host", "192.168.220.3", "--port", "8000"]
