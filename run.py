import argparse
import psutil


def mem_used(process_memory_used):
    """
    Получает память (частный рабочий набор) процесса Windows по имени процесса или PID.
    Args:
        process_memory_used (str или int): Имя процесса или PID.
    Returns:
        float: Память, используемая процессом в мегабайтах (МБ).

    Usage:

    1. Сохраните код в файле с расширением .py, например, mem_usage.py.
    2. Откройте командную строку или терминал.
    3. Перейдите в каталог, где находится скрипт.
    4. Выполните скрипт, указав имя процесса или PID в качестве аргумента командной строки:

    python mem_usage.py <имя_процесса_или_pid>

    Например:
    python mem_usage.py -n chrome.exe или python mem_usage.py -p 2345

    """

    if isinstance(process_memory_used, str):
        # Получить процесс по имени
        process = psutil.Process(process_memory_used)
    else:
        # Получить процесс по PID
        process = psutil.Process(process_memory_used)

        # Получить частный рабочий набор процесса
    result_memory_use = process.memory_info().private / 1024

    return result_memory_use


if __name__ == "__main__":
    # Создать парсер аргументов
    parser = argparse.ArgumentParser(description="Получить память, используемую процессом Windows.")

    # Добавить флаги для имени процесса и PID
    parser.add_argument("-n", "--name", type=str, help="Имя процесса")
    parser.add_argument("-p", "--pid", type=int, help="PID процесса")

    # Разобрать аргументы командной строки
    args = parser.parse_args()

    # Получить имя процесса или PID из аргументов
    if args.name:
        process_name_or_pid = args.name
    elif args.pid:
        process_name_or_pid = args.pid
    else:
        # Запросить имя процесса или PID у пользователя
        process_name_or_pid = input("Введите имя процесса или PID: ")

    # Получить память, используемую процессом
    mem = mem_used(process_name_or_pid)

    # Вывести результат
    print(f"Память, используемая процессом {process_name_or_pid}: {mem:.2f} МБ")
