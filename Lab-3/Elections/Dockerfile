FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
COPY wait-for-it.sh wait-for-it.sh
RUN chmod +x ./wait-for-it.sh
#ENTRYPOINT ["./wait-for-it.sh", "db:5432", "--", "python3", "manage.py", "runserver", "127.0.0.1:8000"]
ENTRYPOINT ["./wait-for-it.sh", "db:5432", "--", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000

