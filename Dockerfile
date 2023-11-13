FROM python:3.10-slim

WORKDIR /
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 9898
CMD [ "python3", "./app.py" ]
