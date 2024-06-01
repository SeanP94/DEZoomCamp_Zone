FROM python:3.10

WORKDIR /path
RUN python -m pip install --upgrade pip


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]