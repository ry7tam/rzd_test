FROM debian:12

LABEL authot="rs7tm"

ENV TZ="Asia/Yekaterinburg"

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update && apt-get install -y apt-utils
RUN apt-get install -y \
    procps \
    watch \
    prometheus-node-exporter \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home
RUN mkdir data

COPY ./conf.d/mem_top10.sh .
COPY ./conf.d/mem_top10_start.sh  .

RUN chmod +x mem_top10.sh
RUN chmod 777 mem_top10.sh
RUN chmod +x mem_top10_start.sh
RUN chmod 777 mem_top10_start.sh
RUN ["bash", "/home/mem_top10_start.sh"]


EXPOSE 9100
# RUN service prometheus-node-exporter start
# RUN watch -n 10 ./mem_top10.sh &>/dev/null &



#CMD ["watch" "-n" "10" "./mem_top10.sh" "&>/dev/null" "&"]
 # CMD ["prometheus-node-exporter", "--collector.textfile.directory=/home/data"]