FROM python:3.9

# Install requirements
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY src/ /app
WORKDIR /app

RUN chmod 444 app.py

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Run the web service on container startup.
CMD [ "python", "app.py" ]
