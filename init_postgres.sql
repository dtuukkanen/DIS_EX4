-- Create tables for wines
CREATE TABLE sparkling_wines (
    id SERIAL PRIMARY KEY,
    wine_type TEXT,
    food_item TEXT,
    food_category TEXT,
    cuisine TEXT,
    pairing_quality INT,
    quality_label TEXT,
    description TEXT
);

CREATE TABLE white_wines (
    id SERIAL PRIMARY KEY,
    wine_type TEXT,
    food_item TEXT,
    food_category TEXT,
    cuisine TEXT,
    pairing_quality INT,
    quality_label TEXT,
    description TEXT
);

CREATE TABLE red_wines (
    id SERIAL PRIMARY KEY,
    wine_type TEXT,
    food_item TEXT,
    food_category TEXT,
    cuisine TEXT,
    pairing_quality INT,
    quality_label TEXT,
    description TEXT
);

CREATE TABLE dessert_wines (
    id SERIAL PRIMARY KEY,
    wine_type TEXT,
    food_item TEXT,
    food_category TEXT,
    cuisine TEXT,
    pairing_quality INT,
    quality_label TEXT,
    description TEXT
);

CREATE TABLE rose_wines (
    id SERIAL PRIMARY KEY,
    wine_type TEXT,
    food_item TEXT,
    food_category TEXT,
    cuisine TEXT,
    pairing_quality INT,
    quality_label TEXT,
    description TEXT
);

-- Create staging
CREATE TABLE staging (
    wine_type TEXT,
    wine_category TEXT,
    food_item TEXT,
    food_category TEXT,
    cuisine TEXT,
    pairing_quality INT,
    quality_label TEXT,
    description TEXT
);

-- Copy data into staging
COPY staging(wine_type,wine_category,food_item,food_category,cuisine,pairing_quality,quality_label,description)
FROM '/docker-entrypoint-initdb.d/wine_food_pairings.csv'
DELIMITER ','
CSV HEADER;

INSERT INTO sparkling_wines (wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description)
SELECT wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description
FROM staging WHERE wine_category = 'Sparkling';

INSERT INTO white_wines (wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description)
SELECT wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description
FROM staging WHERE wine_category = 'White';

INSERT INTO red_wines (wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description)
SELECT wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description
FROM staging WHERE wine_category = 'Red';

INSERT INTO dessert_wines (wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description)
SELECT wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description
FROM staging WHERE wine_category = 'Dessert' AND wine_type <> 'Ice Wine'; /* wine_type = 'Sauternes', works too */

INSERT INTO rose_wines (wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description)
SELECT wine_type,food_item,food_category,cuisine,pairing_quality,quality_label,description
FROM staging WHERE wine_category = 'Rosé';

DROP TABLE staging CASCADE;
