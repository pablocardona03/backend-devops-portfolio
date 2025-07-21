FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc pkg-config default-libmysqlclient-dev build-essential  && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
