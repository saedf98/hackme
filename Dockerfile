# Use the official Python image from the Docker Hub
FROM python:3.11.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update \
  && apt-get install -y gcc libmysqlclient-dev \
  && apt-get clean

# Set the working directory
WORKDIR /hackme

# Install dependencies
COPY ./hackme/requirements.txt /hackme/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY ./hackme/ /hackme/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
