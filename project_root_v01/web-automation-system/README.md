# Web Automation System

This project is a web automation system that includes a FastAPI backend and a Streamlit frontend.

## Project Structure

```
web-automation-system/
├── backend/
│   ├── app/
│   │   ├── \_\_init\_\_.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── services/
│   │   │   ├── \_\_init\_\_.py
│   │   │   ├── screenshot\_service.py
│   │   │   ├── email\_service.py
│   │   └── utils/
│   │       ├── \_\_init\_\_.py
│   │       ├── image\_utils.py
│   ├── tests/
│   │   ├── \_\_init\_\_.py
│   │   ├── test\_main.py
│   │   ├── test\_screenshot\_service.py
│   │   ├── test\_email\_service.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── templates/
│   ├── email\_template.html
├── screenshots/
├── logs/
├── .gitignore
└── README.md
```

## Setup

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/web-automation-system.git
    cd web-automation-system
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

### Environment Variables

Create a `.env` file in the `backend` directory with the following content:

```env
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
EMAIL_USER=user@example.com
EMAIL_PASSWORD=yourpassword
```

### Usage

- The FastAPI backend will be available at `http://localhost:8000`.
- The Streamlit frontend will be available at `http://localhost:8501`.

### CI/CD Pipeline

A GitHub Actions workflow is set up to automate the build and deployment process. Make sure to add the necessary secrets (`DOCKER_USERNAME`, `DOCKER_PASSWORD`, `SSH_PRIVATE_KEY`) in your GitHub repository settings.

### License

This project is licensed under the MIT License.
