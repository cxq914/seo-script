FROM python:3.10

WORKDIR /app

COPY . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
