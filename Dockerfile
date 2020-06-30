FROM python

MAINTAINER openprov "junqzhan@redhat.com"

USER root
RUN pip install openprov

WORKDIR /root/

ENTRYPOINT [ "openprov" ]


