# (1)
FROM python:3.9

# (2)
WORKDIR /app

# (3)
COPY ./requirements.txt /app/requirements.txt

# (4)
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# (5)
COPY . .

# (6)
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]

