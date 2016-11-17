FROM ubuntu:14.04
EXPOSE 5002
MAINTAINER Chet Carello "cpuskarz@cisco.com"

#VOLUME ["/app/data"]

# Install basic utilities
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install setuptools wheel

ADD . /app
WORKDIR /app
RUN pip install -r  requirements.txt

CMD ["python", "./drum2_api.py"]

# notes
# more notes

