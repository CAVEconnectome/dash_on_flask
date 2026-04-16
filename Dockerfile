FROM tiangolo/uwsgi-nginx-flask:python3.10

RUN  git config --global http.sslVerify false && \
     mkdir -p /home/nginx/.cloudvolume/secrets && chown -R nginx /home/nginx && usermod -d /home/nginx -s /bin/bash nginx

COPY requirements.in /app/.
RUN  pip install -r requirements.in
COPY timeout.conf /etc/nginx/conf.d/
COPY . /app
