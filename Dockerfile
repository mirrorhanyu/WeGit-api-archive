FROM frolvlad/alpine-python3

RUN apk add --update alpine-sdk libxslt-dev libffi-dev libxml2-dev openssl-dev postgresql-dev python3-dev

RUN pip3 install virtualenv

WORKDIR /app
COPY ./ /app

EXPOSE 5000

CMD ["sh", "go.sh"]
