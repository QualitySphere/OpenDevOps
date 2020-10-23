FROM bxwill/python:3.8-flask
LABEL maintianer=v.stone@163.com
WORKDIR /workspace
COPY . .
RUN pip install -r requirements.txt
CMD ./launch.sh
EXPOSE 80
