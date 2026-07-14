FROM python:3.14-slim

WORKDIR /app

# Show Python output immediately in Docker/Kubernetes logs
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "monitor.py"]
