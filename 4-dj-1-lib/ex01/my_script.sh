#!/bin/bash

# Show the pip version
python3 -m pip -V

# Remove the existing local_lib folder to ensure a fresh install
rm -rf local_lib

# Install the path module from GitHub into local_lib and log the process
python3 -m pip install git+https://github.com/jaraco/path.git --target=local_lib --upgrade --log pip-install.log

# If the installation was successful, run the Python program
if [ $? -eq 0 ]; then
    echo "Script installation success."
    python3 my_program.py
else
    echo "Script installation failed. Check pip-install.log for details."
fi
