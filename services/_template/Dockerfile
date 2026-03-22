FROM python:3.11-slim

WORKDIR /app

# Copy shared constants into every container
COPY ../shared /app/shared

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY . .

CMD ["python", "app.py"]