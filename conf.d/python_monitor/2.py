# import prometheus_client

# def main():
#     # Создаем объект метрики
#     top_10_memory = prometheus_client.GaugeMetricFamily('top_10_memory', 'Memory usage of top 10 processes', labels={
#         'id': '19',
#         'comman': 'rzd-yes',
#         'memory': '8',
#     })

#     # Устанавливаем значение метрики
#     top_10_memory.set(1027, timestamp=int(time.time()))

#     # Записываем метрики в файл
#     prometheus_client.write_to_file('/home/rystam/Documents/#work/rzd_old/python_monitor/metrics.prom', [top_10_memory])



from prometheus_client import CollectorRegistry, Gauge, write_to_textfile

registry = CollectorRegistry()
g = Gauge('raid_status', '1 if raid array is okay', registry=registry)
g.set(1)
write_to_textfile('/home/rystam/Documents/#work/rzd_old/python_monitor/yes.prom', registry)