#!/bin/bash

# Read URLs from standard input
while IFS= read -r url; do
  # Check if the URL is empty
  if [[ -z "$url" ]]; then
    echo "Empty line detected. Skipping..."
    continue
  fi

  # Use curl with a timeout to get the HTTP status code
  status_code=$(curl -o /dev/null -s --max-time 10 -w "%{http_code}" "$url")
  
  # Check if curl was successful
  if [[ $? -ne 0 ]]; then
    echo "$url - Error: URL not responding or timeout occurred"
  else
    echo "$url - HTTP Status Code: $status_code"
  fi
done
