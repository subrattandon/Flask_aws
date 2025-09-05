# Flask Demo

A simple Flask application demonstrating basic web development and containerization.

## Technologies Used

- **Python 3**
- **Flask**
- **Docker**

## Getting Started

### Prerequisites

- Python 3.x
- Docker

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flask_demo.git
    cd flask_demo
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

```bash
python app.py
```

The app will be available at `http://localhost:5000`.

## Docker Support

You can run the application inside a Docker container.

### Dockerfile

```dockerfile
# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```

### Build and Run with Docker

```bash
docker build -t flask_demo .
docker run -p 5000:5000 flask_demo
```

## License

This project is licensed under the MIT License.