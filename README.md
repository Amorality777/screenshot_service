Веб-сервис получает ссылку на сайт и уровень вложенности и делает скриншоты основной страницы и всех вложенных страниц.

API

- POST /screenshot получает url сайта, уровень вложенности, возвращает id задачи.
- GET /check/\<id> возвращает состояние задачи; если задача завершена: возвращает список идентификаторов изображений.
- GET /screenshot/<id> возвращает ссылку для скачивания скриншота.
