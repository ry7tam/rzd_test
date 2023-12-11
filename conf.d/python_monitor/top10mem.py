import psutil

# Получаем список всех процессов и их использование памяти
all_processes = [proc for proc in psutil.process_iter(["pid", "name", "memory_info"])]

# Сортируем процессы по использованию памяти
sorted_processes = sorted(all_processes, key=lambda x: x.info["memory_info"].rss, reverse=True)

# Выводим информацию о топ-10 процессах
for process in sorted_processes[:10]:
    pid = process.info["pid"]
    name = process.info["name"]
    memory = process.info["memory_info"].rss / 1024 / 1024  # Преобразуем байты в мегабайты
    print(f"PID: {pid}, Наименование: {name}, Память: {memory:.2f} МБ")