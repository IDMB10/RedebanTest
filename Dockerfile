FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \     
    PYTHONUNBUFFERED=1
COPY Pipfile Pipfile.lock* /app/
RUN pip install pipenv && pipenv install --deploy --system
COPY . /app
ENV FLASK_APP=wsgi.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]