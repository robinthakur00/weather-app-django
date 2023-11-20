# Django Weather App

This repository contains a Django web application for retrieving weather information.

## Overview

The Django Weather App provides functionality to fetch weather data for specific locations.

## Prerequisites

- Python (3.x)
- Django framework
- pip (Python package manager)
- Docker
- AWS Account

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/robinthakur00/weather-app-django.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

4. Access the app in a web browser at `http://localhost:8000/`

## File Structure

- `manage.py`: Django management script.
- `weather/`: Main application directory containing models, views, and templates.
- `requirements.txt`: File listing Python dependencies.
- `README.md`: This file, providing project information.

## Usage

- Modify the Django app logic in the `weather/` directory to extend or customize functionality.
- Update HTML templates in the `templates/` directory for UI changes.
- Use additional Django apps or libraries as needed.

## Deploying with Docker

Run the Django app using Docker:

1. **Build Docker Image:**
    ```bash
    docker build -t weather-app-django .
    ```

2. **Run Docker Container:**
    ```bash
    docker run -d -p 8000:8000 --name weather-app-django weather-app-django:latest
    ```

    OR

    **Using Docker Compose:**
    ```bash
    docker-compose down 
    ```
     ```bash
    docker-compose up -d 
    ```
    
3. Access the app in a web browser at `http://localhost:8000/`

## Deploying to AWS with Jenkins Pipeline

Automate deployment using Jenkins Pipeline on AWS:

1. **Set up Jenkins:**
    - Install Jenkins on an AWS EC2 instance.
    - Configure Jenkins with necessary plugins (e.g., Git, AWS).

2. **Create Jenkins Pipeline:**
    - Create a Jenkins job with a Jenkinsfile written in Groovy.

3. **AWS Configuration:**
    - Configure AWS IAM roles for Jenkins to access AWS services.
    - Set up security groups, IAM roles, and permissions for EC2 instances.
    - Configure necessary networking settings to access the application.

4. **Execute Pipeline:**
    - Run the Jenkins Pipeline job to trigger the deployment process.
    - Jenkins Pipeline automates installing dependencies, building Docker images, and deploying the app on AWS.

## Contributing

Contributions are welcome! Fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

