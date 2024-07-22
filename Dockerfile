FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y cowsay fortune netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/games:${PATH}"

COPY wisecow.sh /app/wisecow.sh
#Set work dir
WORKDIR /app
# Give execution permission
RUN chmod +x wisecow.sh

EXPOSE 4499
# RUN wisecow application
CMD ["./wisecow.sh"]
