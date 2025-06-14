# Прогноз риска сердечно-сосудистого заболивания у пациента.

Этот проект представляет собой веб-сервис на FastAPI, который позволяет загружать CSV файлы и просматривать их содержимое в формате JSON.

## Установка

1. Убедитесь, что у вас установлен Python 3.7 или выше

2. Создайте виртуальное окружение:
   !python3 -m venv

3. Активируйте виртуальное окружение:
   !source venv/bin/activate

4. Установите зависимости:
   !python3 -m pip install -r requirements.txt

## Запуск приложения

1. Запустите сервер:
   !uvicorn app:app --host 0.0.0.0 --port 8000

2. Откройте браузер и перейдите по адресу:
   http://localhost:8000

## Использование

1. На главной странице отображается форма для загрузки файла
2. Нажмите кнопку "Выберите файл" и выберите CSV файл
3. Нажмите кнопку "Загрузить"
4. Прогнозы будут отображены на странице в формате JSON