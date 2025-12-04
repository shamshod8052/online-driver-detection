# Base image
FROM python:3.9-slim

# Non-root user
RUN adduser --disabled-password myuser
USER myuser

# Ishchi papka
WORKDIR /code

# Dependencies
COPY --chown=myuser:myuser requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllari
COPY --chown=myuser:myuser . .

# Entrypoint
ENTRYPOINT ["./docker/entrypoint.sh"]

# Default command
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "config.asgi:application"]
