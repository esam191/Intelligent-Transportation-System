# Use the openj JDK 17 as the base image
FROM openjdk

# Create a new app directory for my application files
RUN mkdir /app

# copy the app files from host machine to image fielsystem
COPY .  /app

# set the directory for executing future commands
WORKDIR /app

# Run the main class
CMD java Main.java

