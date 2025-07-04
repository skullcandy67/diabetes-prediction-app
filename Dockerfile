FROM python:3.12
WORKDIR /app

# Install the application dependencies
COPY . /app
RUN pip install -r requirements.txt

# Copy in the source code
EXPOSE 5000

CMD ["python", "./app.py"]