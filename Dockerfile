FROM debian:12

LABEL author="rs7tm"

ENV TZ="Asia/Yekaterinburg"

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update && apt-get install -y apt-utils
RUN apt-get install -y \
    procps \
    prometheus-node-exporter \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home

COPY ./conf.d/data.prom .

EXPOSE 9100

CMD ["prometheus-node-exporter", "--collector.textfile.directory=/home"]
