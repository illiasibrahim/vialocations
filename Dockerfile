FROM python:3


COPY ./requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install -r /app/requirements.txt

WORKDIR /app

ADD . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "8000", "--workers", "3", "core.wsgi:application"]   

# CMD gunicorn --preload \
#     &&  gunicorn core.wsgi:application --bind 0.0.0.0:$PORT