# selenium_cross_language_test

# Start
## Установить виртуальное окружение командой (пример для python3.10)
python3.10 -m venv venv

## Активировать окружение
source venv/bin/activate

## Установить пакеты
pip install -r requirements.txt

## Запустить тесты c выбором английского языка и затем французского языка
pytest --language=es test_items.py
pytest --language=fr test_items.py

## Ожидаемый результат

Тест будет пройден успешно
