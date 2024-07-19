FROM python:3.12
ENV PYTHONUNBUFFERED 1
WORKDIR /web

COPY requirements.txt ./
RUN pip install --upgrade pip \
    pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]