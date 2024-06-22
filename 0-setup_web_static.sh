#!/usr/bin/env bash
# Setup web_static on the web-01 and web-2 servers

# Install nginx
sudo apt update
sudo apt-get install -y nginx

# Create required directories and set permissions
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/web_static

# Create a fake HTML file for testing
file_content=$(cat <<EOF
<html lang="en">
        <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Test HTML File</title>
        </head>
        <body>
                <h1>Hello, Server!</h1>
                <p>This is a test HTML file used for server testing purposes.</p>
                <p>Server date and time: $(date)</p>
        </body>
</html>
EOF
)
echo "$file_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or update symbolic link to point to the test directory
sym_link=/data/web_static/current
if [ -h $sym_link ]; then
    sudo rm -f $sym_link
fi
sudo ln -s /data/web_static/releases/test/ $sym_link

# Configure Nginx to serve from /data/web_static/current/
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.old

sudo sed -i 's/ default_server;/;/g' /etc/nginx/sites-available/default.old

config_file=$(cat <<EOF
server {
    listen 80 default_server;
    server_name web-01.wassimhaimoudi.tech;

    root /data/web_static/current/;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
    add_header X-Served-by $(hostname);
}
EOF
)

echo "$config_file" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Enable the new Nginx configuration by creating a symbolic link
if [ -h /etc/nginx/sites-enabled/default ]
then
	sudo rm -f /etc/nginx/sites-enabled/default
fi
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Test Nginx configuration for syntax errors
sudo nginx -t

# Restart Nginx to apply the changes
sudo service nginx restart
