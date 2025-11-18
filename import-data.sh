#!/bin/bash
set -e

echo "Waiting for MongoDB to be ready..."
sleep 5

echo "Importing CSV data..."

# Import CSV data into staging collection (no auth needed)
mongoimport --host localhost \
  --db wine_db \
  --collection staging \
  --type csv \
  --headerline \
  --file /data/wine_food_pairings.csv

echo "CSV data imported to staging collection successfully"