# using the latest OpenjJDK as the base image
FROM openjdk

# create a new app directory application files
RUN mkdir /app

# copy the app files from host machine to image fielsystem
COPY .  /app

# set the directory for executing future commands
WORKDIR /app

# run the main class
CMD java Main.java