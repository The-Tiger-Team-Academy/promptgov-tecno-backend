# # Use the official Python image as a base
# FROM python:3.9-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN pip install --upgrade pip && \
#     pip install fastapi uvicorn openai pymongo python-dotenv langchain-community python-docx google-cloud-storage langchain docx2pdf
# # Install system dependencies
# # RUN apt-get update && apt-get install -y --no-install-recommends \
# #     build-essential \
# #     python3-dev \
# #     libpq-dev \
# #     && apt-get clean && rm -rf /var/lib/apt/lists/*

# RUN pip install --upgrade pip

# # Set the working directory
# WORKDIR /app

# # Copy the requirements file into the container
# # COPY requirements.txt /app/requirements.txt

# # Install the Python dependencies
# # RUN pip install --no-cache-dir -v -r requirements.txt


# # Copy the rest of the application code
# COPY . /app

# # Expose the port the app runs on
# EXPOSE 8080

# # Start the application with Gunicorn and Uvicorn
# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8080", "--log-level", "info"]




# forserver ttta
# Use an official Python runtime as a parent image
# FROM python:3.11-slim

# # Set the working directory in the container
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     libreoffice \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

# # It's a good practice to install dependencies before copying the entire application to utilize Docker's cache
# # Also, upgrading pip and installing packages in one RUN command reduces the image layers
# RUN pip install --upgrade pip && \
#     pip install fastapi uvicorn openai pymongo python-dotenv langchain-community python-docx google-cloud-storage langchain docx2pdf

# # Copy the current directory contents into the container at /app
# COPY . .

# # Expose the port the app runs on
# EXPOSE 2323

# # Run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2323"]



# Use the official Python image as a base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

RUN apt-get update && apt-get install -y fonts-thai-tlwg

RUN apt-get update && apt-get install -y locales && \
    sed -i -e 's/# th_TH.UTF-8 UTF-8/th_TH.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales
ENV LANG th_TH.UTF-8
ENV LANGUAGE th_TH:th
ENV LC_ALL th_TH.UTF-8


# Install LibreOffice and other dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends libreoffice && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install fastapi uvicorn openai pymongo python-dotenv langchain-community python-docx google-cloud-storage langchain docx2pdf

# Copy the application files to the container
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]



