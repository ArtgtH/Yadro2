FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install requests && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

COPY /task1/script.py .

CMD ["python3", "script.py"]