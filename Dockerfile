FROM python:3.6
COPY ./requirements.txt /app/requirements.txt
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
