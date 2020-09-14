FROM nginx:1.16-alpine
LABEL maintainer="v.stone@163.com"
RUN cd /usr/share/nginx && \
    rm -rf html && \
    mkdir html
WORKDIR /usr/share/nginx/html
COPY . .
CMD ["sh", "run.sh"]
