FROM python:3.9.1

RUN pip install pandas

WORKDIR /app

COPY pipline.py pipeline.py

ENTRYPOINT [ "python", "pipeline.py" ]