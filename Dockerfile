FROM python:3.11.9

WORKDIR /nutrition-api/src

# Copy requirements.txt first to leverage Docker caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# This instruction is commented to fix an issue with volume creation
# COPY . .

EXPOSE 8000

# Uncomment for PROD
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# FastAPI (via uvicorn) does not automatically reload files unless explicitly told to.
# When using mounted volumes during development, use the --reload option:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
