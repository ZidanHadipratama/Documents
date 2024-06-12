FROM openjdk:latest

RUN microdnf install -y gcc
RUN microdnf install -y findutils unzip

RUN useradd -ms /bin/bash web

WORKDIR /

COPY app /app

RUN chown -R web:web /app

WORKDIR /app

RUN curl -L https://services.gradle.org/distributions/gradle-8.7-bin.zip -o gradle-8.7-bin.zip
RUN unzip gradle-8.7-bin.zip -d /opt/gradle
RUN rm gradle-8.7-bin.zip
ENV GRADLE_HOME /opt/gradle/gradle-8.7
ENV PATH $GRADLE_HOME/bin:$PATH

EXPOSE 8090

COPY flag.txt /flag.txt
RUN chown root:root /flag.txt
RUN chmod 400 /flag.txt

COPY readflag.c /readflag.c
RUN gcc /readflag.c -o /readflag
RUN rm /readflag.c

RUN chown root:web /readflag
RUN chmod 4755 /readflag

USER web
RUN gradle build
CMD ["gradle", "bootRun"]
