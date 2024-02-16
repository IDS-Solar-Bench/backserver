FROM python:3.9

RUN pip install paho-mqtt

WORKDIR /usr/app/src

COPY . /usr/app/src/

CMD ["python", "publishData.py"]
