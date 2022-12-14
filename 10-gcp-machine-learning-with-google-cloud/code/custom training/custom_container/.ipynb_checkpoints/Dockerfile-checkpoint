FROM python:3.7-buster
WORKDIR /root
COPY train.py /root/train.py
COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt
ENTRYPOINT ["python", "train.py"]