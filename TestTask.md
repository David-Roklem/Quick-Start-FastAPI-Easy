# Задачи для реализации (техническое задание)

## 1. Аутентификация пользователя (JWT) - файлы users.py, security.py:
   - +Создайте конечную точку регистрации (/auth/register/) пользователя с именем пользователя и паролем. Вместо базы данных можете использовать словарь / массив, как было у нас в курсе. 
   - +Реализовать конечную точку входа пользователя в систему (/auth/login/) для генерации токенов JWT для аутентификации.
   - В файле security.py расположены схема аутентификации (OAuth2 - OAuth2PasswordBearer), функция по созданию JWT-токена, функция по декодированию JWT-токена и функция по извлечению информации о юзере из полезной нагрузки.

## 2. Обмен валюты - файлы currency.py, external_api.py:
   - Внедрить защищенную конечную точку для получения свежих обменных курсов для различных валют из открытого API обменных курсов (/currency/exchange/).
   - Разрешить пользователям выполнять конвертацию валют на основе выбранных обменных курсов в случае подтверждения валидности JWT-токена (используйте класс Depends).
   - Внедрить обработку ошибок для таких случаев, как недопустимые коды валют.
   - Вынесите логику осуществления запроса с внешнего ресурса (API) в отдельный сервис/функции в отдельном файле (как минимум, потребуются функции запросить текущий курс по валютной паре, и запросить список валют (кодов) для получения курса). Обращаться к внешнему сервису из вашего приложения можно с использованием библиотеки requests или aiohttp. 

## 3. Дополнительные маршруты - файл currency.py:
   - Создайте защищенную конечную точку для отображения списка поддерживаемых валют и их кодов (/currency/list/).

## 4. Модели Pydantic - файлы в папке models (альтернативное название этой папки - schemas):
   - Создайте модели Pydantic для автоматической валидации получаемых данных (например, модель юзера - юзернейм/пароль, модель валют - валюта 1, валюта 2, количество для обмена - по умолчанию 1).

## 5. Тестирование - файлы в папке tests:
   - Напишите модульные тесты для реализованных маршрутов и функций.
   - Обеспечьте тестовое покрытие для аутентификации и функциональности обмена валюты.

## 6. Конфигурация среды - файлы .env, config.py:
   - Храните конфиденциальные переменные конфигурации (например, открытый ключ API обменных курсов, секретные настройки для JWT-токена) в файле `.env`. Загрузить настройки приложения можете в файле config.py, например с применением библиотек python-dotenv, environs или pydantic-settings. 

## 7. Руководство по прочтению и использованию:
   - Предоставьте четкие инструкции в README о том, как настроить и запустить проект.
   - Включите примеры запросов API и ответов в README.
   - Перечислите используемые (применяемые в проекте) фичи.

*П.С. для включения в main.py ваших маршрутов из /api/endpoints/ примените знания из урока 8.1 об APIRouter'ах.*