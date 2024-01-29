#!/bin/bash

while true ;do

    # Ask if the user wants to add another file
    read -p "Do you want to add a file? (y/n): " add_file

    if [[ $add_file == "n" ]]; then
        read -p "The commit message: " message
        git commit -m "$message"
        break  # Exit the loop if the user doesn't want to add more files
    fi

    # Get the additional file name
    read -p "Enter the additional file: " additional_file
    

    initial_file=$additional_file

    echo "Processing file: $initial_file"
    touch $initial_file
    echo "#!/usr/bin/python3" > $initial_file
    git add "$initial_file"
    git update-index --chmod=+x "$initial_file"
    
      
done
