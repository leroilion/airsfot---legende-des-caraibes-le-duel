FROM ubuntu

WORKDIR /data

RUN apt update
RUN apt install -y texlive-full
RUN apt install -y build-essential

CMD make


# docker build -f Dockerfile . --tag rules_builder

# windows cmd : docker run --rm --volume %cd%:/data rules_builder
# windows powersheel : docker run --rm --volume ${PWD}:/data rules_builder
# Linux : docker run --rm --volume $(pwd):/data rules_builder
