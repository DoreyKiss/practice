FROM ubuntu
LABEL maintainer="Carlos Nunez <dev@carlosnunez.me>"

USER root
COPY ./web-server.bash /

RUN chmod 755 /web-server.bash
RUN apt -y update
# https://forums.docker.com/t/package-netcat-has-no-installation-candidate-how-to-fix-this/136541
RUN apt -y install netcat-traditional

USER nobody

ENTRYPOINT [ "/web-server.bash" ]
