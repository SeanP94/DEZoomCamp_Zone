FROM python:3.9

RUN pip install pandas

WORKDIR /path
COPY pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]