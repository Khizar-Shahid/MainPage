# Use the official Apache Airflow image as the base
FROM apache/airflow:2.9.3

# Install Scrapy
RUN pip install scrapy

# Optionally, you can add more dependencies or configurations here
# Example: Install other Python packages
# RUN pip install some-other-package

# Set the working directory (optional)
# WORKDIR /opt/airflow

# The CMD instruction starts Airflow; usually, you don't need to specify it when using docker-compose
# CMD ["airflow", "webserver"]
