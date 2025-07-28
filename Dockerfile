FROM python:3.10-slim

WORKDIR /app

COPY app/main.py .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/input /app/output

CMD ["python", "main.py"]
