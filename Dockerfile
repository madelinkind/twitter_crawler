# https://github.com/pypa/pip/issues/6197
# https://python.developreference.com/article/10525241/Can't+install+python+module+with+Dockerfile

FROM python:3.6.8-alpine3.6
COPY . /app
WORKDIR /app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk add --no-cache python3-dev libffi-dev gcc && \
 pip3 install --upgrade pip && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

CMD ["python3", "demo.py"]
