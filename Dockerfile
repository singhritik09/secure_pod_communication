# Use Ubuntu base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y cowsay fortune netcat && \
    rm -rf /var/lib/apt/lists/*

# Copy the script into the container
COPY wisecow.sh /app/wisecow.sh

# Set the working directory
WORKDIR /app

# Make the script executable
RUN chmod +x wisecow.sh

# Expose port 4499
EXPOSE 4499

# Set the command to run the script
CMD ["./wisecow.sh"]

# Update PATH environment variable (if needed for games or other purposes)
ENV PATH="/usr/games:${PATH}"
