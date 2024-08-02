#!/bin/bash
# Check if URL is provided as an argument
#!/bin/bash
curl -s "$1" -o response.txt
wc -c < response.txt
