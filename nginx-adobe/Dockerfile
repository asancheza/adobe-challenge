FROM nginx:alpine

RUN touch /var/run/nginx.pid && \
  chown -R nginx:nginx /var/run/nginx.pid && \
  chown -R nginx:nginx /var/cache/nginx /etc/nginx/

EXPOSE 80

USER nginx

COPY content.html /usr/share/nginx/html/index.html
