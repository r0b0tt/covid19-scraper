FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
COPY ./bin/gunicorn.sh .

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev 

RUN pip install -r requirements.txt

COPY . .



EXPOSE 5000

ENTRYPOINT [ "./gunicorn.sh" ]