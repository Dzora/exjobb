FROM ubuntu:18.04
RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-pip
RUN apt-get install -y --no-install-recommends default-jdk

EXPOSE 1099 50000 5000

# Run the application:
COPY /src /src
# Install dependencies:
RUN pip3 install -r src/requirements.txt
CMD ["python3", "src/app.py"]
