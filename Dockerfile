# https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
FROM python:3.6-alpine as base
FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
