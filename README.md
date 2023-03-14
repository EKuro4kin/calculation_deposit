# Приложение "Calculation of the deposit"
Предоставляет возможности произвести расчёт депозита. Предоставляет список суммы
вклада, с учётом ежемесячного прироста от фиксированного процента.

## стек (python3.9, Flask, HTML)


### Перед началом работы:

#### Установка зависимостей:

В корневой папке находиться файл с зависимостями requirements.txt
```shell
pip install -r requirements.txt
```

#### Развертывание приложение:

Для удобства имеется файл Dockerfile позволяющий запустить приложение из контейнера

````shell
docker build -t 'вводится имя докерфайла' .
docker run -d -p 5000:5000 'вводится имя докерфайла' 
````

#### Настройка переменных окружения:

Для работы проекта необходимо создать **.venv** в корневой папке.
В нем нужно указать необходимые значения переменных:

* DEBUG=True (или False) - **включения или выключения дебагера flask**


### Запуск REST API приложения на Flask:

```shell
python ./app.py
```
