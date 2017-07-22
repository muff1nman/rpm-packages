FROM docker.io/fedora:26

# Atomic RUN label, enables the atomic cli
LABEL RUN='docker run --name ssh -d -p 2200:22 $IMAGE'

EXPOSE 22

RUN dnf -y update && \
    dnf -y install \
            openssh-server \
            passwd \
            java-1.8.0-openjdk-headless \
            gnupg2 \
            tito && \
    dnf clean all

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
