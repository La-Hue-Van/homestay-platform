FROM python:3.11-slim

WORKDIR /app

COPY shared /app/shared

COPY _template/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY _template/ .

CMD ["python", "app.py"]