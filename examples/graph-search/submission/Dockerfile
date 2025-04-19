FROM condaforge/miniforge3
WORKDIR /src
VOLUME ["/src", "/input", "/output"]

RUN mkdir -p /src /input /output

# You should install any dependencies you need here.
RUN pip install geopy
