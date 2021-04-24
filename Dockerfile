FROM Python:3.7.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /ApiAuth
WORKDIR /ApiAuth
ADD requirements.txt /ApiAuth/
RUN pip install -r requirements.txt
ADD . /ApiAuth/