FROM fedora:37

RUN dnf install -y python3 python3-pip

RUN pip3 install requests bs4 html5lib

COPY --chmod=0755 ding.py /usr/bin/
