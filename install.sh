#!/bin/bash
# Network0ptimizer install script

echo "Installing Network0ptimizer..."

# Install git and python3 if missing (optional, good idea)
if ! command -v git &> /dev/null; then
    echo "Git not found, installing..."
    sudo apt update && sudo apt install -y git
fi

if ! command -v python3 &> /dev/null; then
    echo "Python3 not found, installing..."
    sudo apt update && sudo apt install -y python3
fi

# Clone the repository
git clone https://github.com/next-ninja/Network0ptimizer.git

# Move into the project directory
cd Network0ptimizer || exit

# Optionally install Python requirements if you have requirements.txt
# if [ -f "requirements.txt" ]; then
#     echo "Installing Python dependencies..."
#     python3 -m pip install -r requirements.txt
# fi

# Make optimizer.py executable (optional)
chmod +x optimizer.py

# Run the optimizer script
echo "Running optimizer.py..."
python3 optimizer.py
