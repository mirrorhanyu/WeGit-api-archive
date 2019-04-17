FROM frolvlad/alpine-python3

RUN pip3 install virtualenv

WORKDIR /app
COPY ./ /app

EXPOSE 5000

CMD ["sh", "go.sh"]