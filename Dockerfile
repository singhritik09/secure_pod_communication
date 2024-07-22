FROM alpine:latest

RUN apk --no-cache add fortune cowsay bash netcat-openbsd

COPY wisecow.sh /usr/local/bin/wisecow.sh

RUN chmod +x /usr/local/bin/wisecow.sh

EXPOSE 4499

CMD ["/usr/local/bin/wisecow.sh"]
