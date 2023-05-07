#!/bin/bash

echo "Installing pillow..."
pip install pillow
if [ $? -ne 0 ]; then
    echo "Failed to install pillow. Please try again."
    read -p "Press enter to continue"
    exit 1
fi

echo "Installing requests..."
pip install requests
if [ $? -ne 0 ]; then
    echo "Failed to install requests. Please try again."
    read -p "Press enter to continue"
    exit 1
fi

echo "Installing pyperclip..."
pip install pyperclip
if [ $? -ne 0 ]; then
    echo "Failed to install pyperclip. Please try again."
    read -p "Press enter to continue"
    exit 1
fi

echo "All requirements have been installed."
read -p "Press enter to continue"
exit 0
