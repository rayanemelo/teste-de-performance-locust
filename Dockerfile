FROM python:3.9-slim

WORKDIR /app
 
COPY requirements.txt ./
COPY locustfile.py ./

RUN pip install --no-cache-dir -r requirements.txt
 
COPY . .
 
CMD ["locust", "-f", "locustfile.py"]