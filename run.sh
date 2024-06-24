#!/bin/bash

is_installed() {
    python3 -c "import $1" &> /dev/null
    return $?
}

if ! is_installed pandas; then
    echo "Pandas is not installed. Installing pandas..."
    pip install pandas

    if is_installed pandas; then
        echo "Pandas installed successfully."
    else
        echo "Failed to install pandas. Exiting."
        exit 1
    fi
fi

python3 main.py