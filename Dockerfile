# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Install cron
RUN apt-get update && apt-get -y install cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

# create root directory for our project in the container
RUN mkdir /news_board

# Set the working directory to /music_service
WORKDIR /news_board

# Copy the current directory contents into the container at /music_service
ADD . /news_board/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
