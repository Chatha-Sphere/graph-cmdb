FROM python:3.6
COPY ./requirements.txt /app/requirements.txt
#COPY ./start.sh /app/start.sh
COPY ./app /app
WORKDIR /app
#RUN chmod +x /start.sh
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
