# rzd_test

Для запуска необходимо:

1. `conf.d/prometheus.yml` - поменять ip adress targets
2. `docker build -t deb-mon .` Необходимо построить image для контейнера, который мы мониторим 
2. `docker-compose up -d` - поднимаем связку необходимых контейнеров
3. `http://localhost:3000/connections/datasources` В веб интерфейсе Grafana поменять ip adress datasource 

Смотрим dashboards   "Linux Hosts Metrics | Base" & "top_10_mem"

Для мониторинга топ10 процессов подкладываю готовый файл data.prom, полноценный скрипт для мониторинга топ 10 процессов так и не разработал, такой завал был.. поработал с библиотеками python и Go, наработки положил в conf.d, в целом всё понятно, но как обычно бывает "всё кроется в мелочах", в случае "необходимости" разберусь и с ними



