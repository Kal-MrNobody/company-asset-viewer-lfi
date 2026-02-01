FROM python:3.9-slim
WORKDIR /app
COPY useragent.py .
RUN pip install --no-cache-dir flask
EXPOSE 5080
CMD ["python", "useragent.py"]
