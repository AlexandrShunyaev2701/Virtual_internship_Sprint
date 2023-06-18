Это API для мобильного приложения, которым могут пользоваться туристы для отправки данных о горных перевалах и отправки их в Федерацию Спортивного Туризма России (ФСТР).
Когда туристы добираются до горного перевала, они могут сделать снимки и использовать мобильное приложение для отправки информации. Как только турист нажимает "Отправить", мобильное приложение вызывает метод submitData, который принимает данные в формате JSON.
Результатом отправки является статус и сообщение о состоянии: { "status": 200, "message": "OK"}.

Модели
Users
Модель пользователей, содержит информацию о пользователе: email, пароль, имя, фамилию, отчество.

Pereval
Модель перевалов, содержит информацию о перевалах: название, красивое название, координаты, изображения, статус, дата добавления, идентификатор пользователя, который добавил перевал.

Coords
Модель координат, содержит информацию о координатах перевалов: широту, долготу и высоту.

Images
Модель изображений перевалов, содержит информацию об изображении и его названии.

Level
Модель уровней. Содержащая уровень сложности преодоления перевала в каждый сезон.


API методы:
GET /submitData/ method
Возвращает список всех горных перевалов.

POST /submitData/ method
Позволяет создать запись об одином горном перевале.

GET /submitData/{id}
Извлекает данные для конкретного горного перевала.

PATCH /submitData/{id}
Позволяет изменять значения атрибутов записи о горном перевале.
В качестве результата вернется сообщениеЮ содержащие:
state:
состояние: 1 для успешного обновления и 0 для неуспешного обновления
message: объясняет, почему изменение завершилось неудачно

GET/submit Data/?user__email=<email>
Возвращает список данных обо всех объектах, которые пользователь с данным email отправил на сервер.
