# Pull office base image
FROM python:3.10-slim

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y python3-dev build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv

# Create virtual environment and upgrade pip
RUN pip install --upgrade pip && \
    pip install virtualenv && \
    python -m virtualenv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Add and install requirements
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy the application code
COPY . /srv/app
WORKDIR /srv/app

# Optional: Collect static files if using Django
# RUN python manage.py collectstatic --noinput
