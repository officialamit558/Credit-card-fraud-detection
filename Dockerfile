# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source
COPY . .

# Expose port and start application
EXPOSE 5000
CMD ["python", "app.py"]