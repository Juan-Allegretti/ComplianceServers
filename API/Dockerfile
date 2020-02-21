FROM python:3.7
ADD requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /
WORKDIR /
ADD . /
CMD ["python3", "init_app.py"]
