# Скрипты для исправления оценок, удаления замечаний и созданий похвал в электронном дневнике

Проект имеет три основные возможности:
* Исправляет оценки: "двойки" и "тройки" на "пятерки"
* Удаляет замечания
* Добавляет похвалы по выбранному предмету

### Инструкция по использованию

Для работы кода требуется работающий доступ к электронному дневнику школы
* Запустите командную строку сайта командой  
`python manage.py shell`
* Скопируйте код из файла scripts.py и вставьте его в командную строку

### Как запустить электронный дневник

- Скачайте код c сайта github:  
`git clone https://github.com/devmanorg/e-diary`
- Установите зависимости командой  
`pip install -r requirements.txt`
- Создайте БД командой  
`python3 manage.py migrate`
- Скачайте и добавьте действующую базу данных в папку с кодом.
- Запустите сервер командой  
`python3 manage.py runserver`

#### 1. Исправляем оценки.
* Вставьте строку в командную строку:  
`fix_marks("Иванов Иван")`
* Вместо имени "Иванов Иван" укажите имя ученика, оценки которого необходимо исправить.

#### 2. Удаляем замечания.
* Вставьте строку в командную строку:  
`remove_chastisements("Иванов Иван")`
* Вместо имени "Иванов Иван" укажите имя ученика, замечания которого необходимо удалить.

#### 3. Создаем похвалу.
* Вставьте строку в командную строку:  
`create_commendation("Иванов Иван", "Музыка")`
* Вместо имени "Иванов Иван" укажите имя ученика, похвалу для которого необходимо создать.
* Вместо "Музыка" укажите название предмета, по которому требуется похвала.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).