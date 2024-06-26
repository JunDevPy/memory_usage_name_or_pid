**Описание работы скрипта:**

**mem_usage**

Этот репозиторий содержит Python-скрипт, который позволяет получить память (частный рабочий набор), используемую процессом Windows, по его имени или PID.

**Особенности:**

* Получение памяти в мегабайтах (МБ).
* Поддержка как имен процессов, так и PID.
* Удобный интерфейс командной строки.

**Установка:**

1. Клонируйте репозиторий: `git clone https://github.com/examples/mem_usage.git`
2. Установите зависимости: `pip install -r requirements.txt`

**Использование:**

1. Откройте командную строку или терминал.
2. Перейдите в каталог, где находится скрипт `mem_usage.py`.
3. Выполните скрипт, указав имя процесса или PID в качестве аргумента командной строки:

```
python mem_usage.py [-n <имя_процесса>] [-p <PID>]
```

Например:

* Чтобы получить память, используемую процессом Chrome, выполните: `python mem_usage.py -n chrome.exe`
* Чтобы получить память, используемую процессом с PID 2345, выполните: `python mem_usage.py -p 2345`

**Вклад:**

Мы приветствуем вклады в этот репозиторий. Пожалуйста, ознакомьтесь с рекомендациями по внесению изменений перед отправкой запросов на слияние.
