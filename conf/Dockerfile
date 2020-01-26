FROM nginx:1.15-alpine 

RUN apk add inotify-tools certbot openssl

WORKDIR /opt

COPY ../scripts/entrypoint.sh nginx-letsencrypt
COPY ../scripts/certbot.sh certbot.sh
COPY nginx-prod.conf /etc/nginx/conf.d/default.conf
COPY ssl-options/ /etc/ssl-options

RUN chmod +x nginx-letsencrypt && \
    chmod +x certbot.sh 

ENTRYPOINT ["./nginx-letsencrypt"]