# Use the official Nginx image as a base
FROM nginx:alpine

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy the necessary files into the Nginx web directory
COPY challenge1.html /usr/share/nginx/html/challenge1.html
COPY index.html /usr/share/nginx/html/index.html
COPY SECRETS.txt /usr/share/nginx/html/SECRETS.txt
COPY style.css /usr/share/nginx/html/style.css
COPY style01.css /usr/share/nginx/html/style01.css

# Expose port 80 to allow external access to the container
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
