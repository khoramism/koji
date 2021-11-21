FROM python:3.9.6-alpine
ENV PYTHONUNBUFFERED 1
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
# install psycopg2 dependencies
EXPOSE 8000
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app/
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . /usr/src/app/
CMD while ! python manage.py sqlflush > /dev/null 2>&1 ; do sleep 1 ; done &&\
	python manage.py makemigrations --noinput && \
	python manage.py migrate --noinput && \ 
	python manage.py collectstatic --noinput && \
	gunicorn --chdir /usr/src/app/ --bind :8000 koji.wsgi:application
