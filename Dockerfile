FROM python:3.9-slim

WORKDIR /home/lad-web-scrapper

RUN python -m venv venv
RUN . venv/bin/activate

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt; exit 0
RUN pip install gunicorn

COPY project project
COPY app.py boot.sh config.py ./

RUN chmod a+x boot.sh
ENV FLASK_APP app.py

EXPOSE 8080
ENTRYPOINT ["./boot.sh"]