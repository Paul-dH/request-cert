FROM python:latest

LABEL maintainer="paul@den-hertog.net"
# EXPOSE 8080/tcp

# ARG GIT_REPO

ENV GIT_REPO $GIT_REPO
ENV redirect examples/dashboard.html

RUN ["mkdir", "-p", "/code/template_files"]

RUN apk add --no-cache git python3 py3-pip && python3 -m pip install --upgrade pip

RUN git clone ${GIT_REPO} /code/template_files

WORKDIR /code

RUN npm install -g npm gulp gulp-cli

RUN touch template_files/index.html
RUN /bin/echo -e "<meta http-equiv=\"refresh\" content=\"0; URL='http://localhost:8080/$redirect'\" />" > template_files/index.html

ENTRYPOINT ["python3", "-m", "http.server", "--bind", "0.0.0.0", "--directory", "/code/template_files", "8080"]