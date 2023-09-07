#!/bin/bash

# Ask the user for the desired filename
read -p "Enter the filename (without extension): " filename

# Check if the filename is provided
if [ -z "$filename" ]; then
  echo "Filename cannot be empty. Exiting."
  exit 1
fi

# Create the Python file with the shebang
cat <<EOL > "$filename"
#!/usr/bin/python3

EOL

# Make the file executable
chmod +x "$filename"

echo "$filename created with shebang '#!/usr/bin/python3' and set as executable."
