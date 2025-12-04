# Base image
FROM python:3.12-slim

# Ishchi papka
WORKDIR /code

# Dependensiyalarni ko‘chirish va o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani ko‘chirish
COPY . .

# Daphne bilan ASGI serverni ishga tushirish
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "your_project_name.asgi:application"]
