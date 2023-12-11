import psutil
from prometheus_client import start_http_server, Gauge

# Создаем гистограммы для метрик
memory_usage = Gauge("process_memory_usage_bytes", "Memory usage in bytes", ["pid", "name"])

# Получаем список всех процессов и их использование памяти
all_processes = [proc for proc in psutil.process_iter(["pid", "name", "memory_info"])]

# Сортируем процессы по использованию памяти
sorted_processes = sorted(all_processes, key=lambda x: x.info["memory_info"].rss, reverse=True)

# Обновляем метрики для каждого процесса
for process in sorted_processes[:10]:
    pid = process.info["pid"]
    name = process.info["name"]
    memory = process.info["memory_info"].rss

    # Обновляем значение метрики
    memory_usage.labels(pid=pid, name=name).set(memory)

# Запускаем HTTP-сервер для выдачи метрик
if __name__ == '__main__':
    start_http_server(8000)
    while True:
        for process in sorted_processes[:10]:
            pid = process.info["pid"]
            name = process.info["name"]
            memory = process.info["memory_info"].rss / 1024 / 1024  # Преобразуем байты в мегабайты
            print(f"PID: {pid}, Наименование: {name}, Память: {memory:.2f} МБ")

