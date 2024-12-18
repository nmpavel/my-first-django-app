FROM python:3.12.3

ENV PYTHONUNBUFFERED  1

WORKDIR /app
COPY . .

COPY  requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "/app/django.sh" ]