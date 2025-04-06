# Use the official nginx image as base
FROM --platform=linux/amd64 nginx:latest

# Copy your custom Nginx configuration
COPY ./docker/deploy/nginx/nginx.conf /etc/nginx/conf.d/app.conf

# Copy the built static files from your project into the Nginx html directory.
# Adjust the source folder as needed (e.g., "static", "build", etc.)
COPY ./webapp/static /static/

# Expose ports
EXPOSE 82
