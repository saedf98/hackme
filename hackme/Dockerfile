# Use the official Python image from the Docker Hub
FROM python:3.11.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update \
  && apt-get install -y gcc default-mysql-client default-libmysqlclient-dev \
  && apt-get clean

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /hackme

# Install dependencies
COPY ./requirements.txt /hackme/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY ./ /hackme/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
