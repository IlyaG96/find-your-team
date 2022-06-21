# FindYourTeam

## В разработке. Мэтчинг-сервис для начинающих программистов.

### Вся информация в assignment.yaml

### Интро
<details>
<summary>
Открой меня :)
</summary>
В начале своего пути любой программист без опыта сталкивается с проблемой: отсутствие опыта работы. Частично компенсировать ее может хорошее портфолио на github с пет-проектами.
Но кроме пет-проектов, требуются также навыки работы в команде и навыки использования инструментов разработки и коммуникации разработчиков.
В данный момент крайне сложно или невозможно найти себе команду, потому что нет специализированного и простого сервиса для поиска программистов схожего уровня в свою команду.
Команда получается или слишком неоднородной по опыту: от "новичков" до "джунов", или не может выбрать для себя проект по силам.
Данный проект ставит перед собой цель создания мэтчинг-сервиса для программистов, который бы помог новичкам (и не только) собираться в команды и подбирать себе проекты "по силам".

</details>


### Системные требования

- Docker и docker-compose [Как установить Docker?](https://help.reg.ru/hc/ru/articles/4408047640977-%D0%9A%D0%B0%D0%BA-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-Docker-%D0%BD%D0%B0-Ubuntu)
- DockerDesktop для MacOS и Windows [скачать](https://www.docker.com/products/docker-desktop/)
- Python 3.10
- Postgres [Как установить?](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

### Как запустить dev-версию продукта


Создайте в директории find-your-team две переменных окружения:
1) `.env`.

- `DEBUG`= настройка Django для включения отладочного режима. Принимает значения `TRUE` или `FALSE`. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DEBUG).
- `SECRET_KEY`= обязательная секретная настройка Django. Это соль для генерации хэшей. Значение может быть любым, важно лишь, чтобы оно никому не было известно. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key).
- `ALLOWED_HOSTS`= настройка Django со списком разрешённых адресов. Если запрос прилетит на другой адрес, то сайт ответит ошибкой 400. Можно перечислить несколько адресов через запятую, например `127.0.0.1,192.168.0.1,site.test`. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).
- `DATABASE_URL`= адрес для подключения к базе данных PostgreSQL. Другие СУБД сайт не поддерживает. [Формат записи](https://github.com/jacobian/dj-database-url#url-schema).
- `CSRF_COOKIE_DOMAIN`= `http://127.0.0.1:1337`, `http://mydomain.ru`, `https://mydomain.ru` [Документация](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-cookie-domain).
- `CSRF_TRUSTED_ORIGINS`= `http://127.0.0.1:1337`, `http://mydomain.ru`, `https://mydomain.ru` [Документация](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins).

#### ВАЖНО! В переменной `DATABASE_URL` вместо localhost(или db) используйте `host.docker.internal` если необходимо подключиться к postgres на локальном сервере.  
#### В остальных случаях: postgres://postgres:postgres@db:5432/postgres

2) `.env.db`.

- `POSTGRES_USER`=`postgres` - если БД должна находиться в контейнере.
- `POSTGRES_PASSWORD`=`postgres` - если БД должна находиться в контейнере.
- `POSTGRES_DB`=`postgres` - если БД должна находиться в контейнере.

Выполните команду:
```shell
docker-compose -f docker-compose.dev.yaml up --build
```

После успешной сборки приложения, оно будет доступно по [по адресу http://127.0.0.1:1337/admin](http://127.0.0.1:1337/admin)

### Другие способы запуска приложения не рекомендуются