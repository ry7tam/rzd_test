import psutil
from prometheus_client import start_http_server, Summary

# Создать метрик для отслеживания использования памяти
MEMORY_USAGE = Summary('memory_usage_bytes', 'Memory usage in bytes')

# Декорировать функцию с метрикой
@MEMORY_USAGE.time()
def get_top_10_processes():
    """Получить список топ 10 процессов по использованию памяти."""

    # Получить список всех запущенных процессов
    processes = psutil.process_iter()

    # Сортировать процессы по использованию памяти
    processes.sort(key=lambda process: process.memory_info().rss, reverse=True)

    # Получить топ 10 процессов
    top_10_processes = processes[:10]

    # Вернуть список топ 10 процессов
    return top_10_processes


if __name__ == 'main':
    # Запустить HTTP-сервер для доступа к метрикам
    start_http_server(8000)

    while True:
    # Получить список топ 10 процессов
        top_10_processes = get_top_10_processes()

    # Вывести информацию о топ 10 процессах
        for process in top_10_processes:
            print(f"PID: {process.pid()}, Имя: {process.name()}, Использование памяти: {process.memory_info().rss} байт")