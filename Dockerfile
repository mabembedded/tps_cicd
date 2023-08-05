ARG BASE_NAME=debian
ARG IMAGE_ARCH=linux/arm64
ARG IMAGE_TAG=3-bookworm
ARG DOCKER_REGISTRY=torizon

FROM --platform=$IMAGE_ARCH $DOCKER_REGISTRY/$BASE_NAME:$IMAGE_TAG

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    python3-setuptools \
    python3-flask \
    && apt-get clean && apt-get autoremove && rm -rf /var/lib/apt/lists/*

RUN mkdir flaskapp
COPY flaskapp.py /flaskapp/
