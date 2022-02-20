FROM python:3.9-slim
COPY proxy.py proxy.py
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "proxy:app", "--host", "0.0.0.0", "--port", "80"]