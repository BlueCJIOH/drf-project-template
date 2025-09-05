FROM python:3.12-slim AS builder
RUN pip install --no-cache-dir uv
WORKDIR /app
COPY requirements.uv.lock ./
RUN uv pip install --system --requirement requirements.uv.lock

FROM python:3.12-slim AS runtime
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY . .
# To run as non-root, uncomment the following line
# USER 1000
CMD ["uv", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]
