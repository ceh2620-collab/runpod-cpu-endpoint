FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Force rebuild
RUN echo "rebuild_$(date)" > /tmp/rebuild_tag

ENTRYPOINT ["python", "runpod_worker.py"]
