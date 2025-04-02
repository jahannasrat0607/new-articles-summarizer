# Use an official Python image
FROM python:3.9

# Create a non-root user for security
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy application files
COPY --chown=user . /app

# Expose the FastAPI port
EXPOSE 7860

# Start FastAPI app
CMD uvicorn api.main:app --host 0.0.0.0 --port 7860
