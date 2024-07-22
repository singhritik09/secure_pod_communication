FROM debian:latest

RUN apt-get update && apt-get install -y fortune cowsay bash netcat && apt-get clean

COPY wisecow.sh /usr/local/bin/wisecow.sh
RUN chmod +x /usr/local/bin/wisecow.sh

EXPOSE 4499

CMD ["/usr/local/bin/wisecow.sh"]
