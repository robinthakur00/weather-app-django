# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file
COPY requirements.txt /code/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy the Django project code to the container
COPY . /code/

# Expose the port that the Django app will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
