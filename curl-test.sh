#!/bin/bash


RAND=$RANDOM
 
echo "POST"
RESPONSE=$(curl --request POST http://localhost:5000/api/timeline_post -d "name=Elane&email=elane@uci.edu&content=Random test post $RAND")
echo "$RESPONSE"
 
echo ""
echo "GET"
curl http://localhost:5000/api/timeline_post
 
echo ""
ID=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])")
echo "DELETE the test post we just created (id=$ID):"
curl --request DELETE http://localhost:5000/api/timeline_post/$ID
echo ""
 