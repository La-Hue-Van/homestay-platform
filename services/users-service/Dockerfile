FROM python:3.11-slim

WORKDIR /app

# shared folder is now accessible because build context is services/
COPY shared /app/shared

COPY users-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY users-service/ .

CMD ["python", "app.py"]