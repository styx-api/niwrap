FROM ubuntu:20.04

# other containers have encoding issues - I think this fixes it
ENV FSLDIR="/usr/local/fsl" \
    DEBIAN_FRONTEND="noninteractive" \
    LANG="en_GB.UTF-8" \
    LC_ALL="en_GB.UTF-8"

# install dependencies and download installer
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        dc \
        file \
        libgomp1 \
        libgtk2.0-0 \
        libquadmath0 \
        locales \
        python3 \
        wget && \
    locale-gen en_GB.UTF-8 && \
    mkdir -p /usr/local/fsl

# download and verify installer
RUN wget -q https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/releases/fslinstaller.py && \
    ls -l fslinstaller.py

# run installer
RUN python3 fslinstaller.py \
    -d /usr/local/fsl \
    --skip_registration \
    --no_matlab \
    --cuda none \
    --fslversion 6.0.6 \
    --overwrite

# cleanup
RUN rm -f fslinstaller.py && \
    apt-get remove -y wget && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="${FSLDIR}/bin:${PATH}"

WORKDIR /data

RUN echo ". ${FSLDIR}/etc/fslconf/fsl.sh" >> /root/.bashrc

SHELL ["/bin/bash", "-c"]
CMD ["/bin/bash"]