FROM python:3.8-slim-buster

# Update the package lists and install awscli
RUN apt update -y && apt install awscli -y

WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variables if needed
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Specify the command to run the application
CMD ["python", "app.py"]
