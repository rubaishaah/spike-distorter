FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libportaudio2 \
    && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]
