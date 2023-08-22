FROM ubuntu:18.04
# Use this on Apple silicon machines, otherwise the image cannot be built
# FROM --platform=linux/amd64 ubuntu:18.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -qqy wget build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

RUN echo 'export PATH=/opt/miniconda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/miniconda && \
    rm ~/miniconda.sh


RUN mkdir -p /backend
COPY ./backend/requirements.yml /backend/requirements.yml
RUN /opt/miniconda/bin/conda env create -f /backend/requirements.yml
ENV PATH /opt/miniconda/envs/backend/bin:$PATH

ENV PYTHONDONTWRITEBYTECODE 1
RUN echo "source activate backend" >~/.bashrc

COPY ./backend /backend
WORKDIR /backend
