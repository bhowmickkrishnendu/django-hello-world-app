# Use an official Python image as the base image
FROM python:3.11

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Run migrations
RUN python manage.py migrate

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
