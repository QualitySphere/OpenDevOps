FROM busybox
RUN mkdir /harbor_installer && \
    mkdir /workspace && \
    cd /harbor_installer && \
    wget https://github.com/goharbor/harbor/releases/download/v2.1.0/harbor-offline-installer-v2.1.0.tgz -O harbor.tgz && \
    tar zvxf harbor.tgz && \
    rm -rf harbor.tgz 
CMD mv /harbor_installer/harbor/* /workspace/
