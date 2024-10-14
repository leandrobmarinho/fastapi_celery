FROM python:3.11-slim

WORKDIR /app

# set env variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONPATH=/app:/config:/models:/schemas
# ENV PYTHONPATH=/:/app:/config:/models:/schemas

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
