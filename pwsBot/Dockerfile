FROM python:3.11

WORKDIR /app

COPY bot.py requirements.txt ./
COPY resource/ ./resource
COPY commands/ ./commands
COPY voice/ ./voice

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "bot.py" ]
