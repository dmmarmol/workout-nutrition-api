FROM python:3.11.9

WORKDIR /nutrition-api/src

# Copy requirements.txt first to leverage Docker caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["python", "./main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
