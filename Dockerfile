FROM python:3.9

WORKDIR /nutrition-api/src

COPY . ./

RUN pip install --no-cache-dir pipenv && pipenv install

# COPY *.py .

CMD ["python", "./main.py"]
