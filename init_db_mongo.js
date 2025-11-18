// MongoDB initialization script for wine collections

// Authenticate and switch to the database
db = db.getSiblingDB('wine_db');

print("Processing wine data...");

// Helper function to create collection from staging
function createWineCollection(categoryMatch, collectionName) {
    var pipeline = [
        { $match: categoryMatch },
        {
            $addFields: {
                pairing_quality: { $toInt: "$pairing_quality" }
            }
        },
        {
            $project: {
                wine_type: 1,
                food_item: 1,
                food_category: 1,
                cuisine: 1,
                pairing_quality: 1,
                quality_label: 1,
                description: 1
            }
        },
        { $out: collectionName }
    ];

    db.staging.aggregate(pipeline);
    var count = db[collectionName].countDocuments();
    print(collectionName + " collection created with " + count + " documents");
    return count;
}

// Wait for import to complete by checking if staging has data
var maxRetries = 10;
var retryCount = 0;
while (retryCount < maxRetries) {
    var stagingCount = db.staging.countDocuments();
    if (stagingCount > 0) {
        print("Found " + stagingCount + " documents in staging collection");
        break;
    }
    print("Waiting for data import... (attempt " + (retryCount + 1) + "/" + maxRetries + ")");
    retryCount++;

    // Can't sleep in init scripts, but the import should be done by now
    if (retryCount >= maxRetries) {
        print("ERROR: No data found in staging collection after waiting");
        quit(1);
    }
}

// Create collections for each wine category
createWineCollection({ wine_category: "Sparkling" }, "sparkling_wines");
createWineCollection({ wine_category: "White" }, "white_wines");
createWineCollection({ wine_category: "Red" }, "red_wines");
createWineCollection({ wine_category: "Fortified" }, "fortified_wines");
createWineCollection({ wine_category: "Dessert", wine_type: "Ice Wine" }, "ice_wines");

// Create indexes for all collections
var collections = ["sparkling_wines", "white_wines", "red_wines", "fortified_wines", "ice_wines"];

collections.forEach(function(collectionName) {
    db[collectionName].createIndex({ "wine_type": 1 });
    db[collectionName].createIndex({ "food_category": 1 });
    db[collectionName].createIndex({ "cuisine": 1 });
    db[collectionName].createIndex({ "pairing_quality": -1 });
    print("Indexes created for " + collectionName);
});

// Clean up staging collection
db.staging.drop();
print("Staging collection dropped");

print("MongoDB initialization complete!");