# Restaurant Management System - DIS Exercise 4

A multi-database restaurant management system demonstrating transparent integration of PostgreSQL (SQL) and MongoDB (NoSQL) databases through a unified frontend interface.

## Prerequisites
- **Docker & Docker Compose** - For running databases
- **UV** - Python package manager ([Install](https://docs.astral.sh/uv/))

## Quick Start

1. **Start the databases:**
   ```bash
   docker compose up -d
   ```

2. **Run the application:**
   ```bash
   uv run restaurant
   ```

3. **Stop the system:**
   ```bash
   docker compose down
   ```

## Project Requirements & Grading

| Requirement | Implementation | Evidence | Points |
|------------|----------------|----------|--------|
| PostgreSQL database | ✅ PostgreSQL 16 in Docker | compose.yaml, init_postgres.sql | 1.0 |
| MongoDB database | ✅ MongoDB 7 in Docker | compose.yaml, init_db_mongo.js | 1.0 |
| PostgreSQL: 5 tables + data | ✅ orders, customers, menu_items, restaurants, staff | 39 rows total | 1.5 |
| MongoDB: 5 collections + data | ✅ orders, customers, menu_items, reviews, promotions | 33 documents total | 1.5 |
| Print functionality | ✅ Separate & joined views | [PG]/[MG] tags in joined views | 1.25 |
| Insert functionality | ✅ Transparent routing | Works for all categories | 1.25 |
| Delete functionality | ✅ Smart cross-database deletion | Confirmation + automatic routing | 1.25 |
| Modify functionality | ✅ Transparent updates | Updates across databases | 1.25 |
| **TOTAL** | | | **10.0** |

## Data Distribution

**Three Similar Tables** (same schema, different data):
- **orders**: 8 in PostgreSQL (O001-O008), 6 in MongoDB (O009-O014)
- **customers**: 6 in PostgreSQL (C001-C006), 4 in MongoDB (C007-C010)
- **menu_items**: 12 in both databases (M001-M012, same items, different details)

**Two Different Tables per Database**:
- **PostgreSQL only**: restaurants (5), staff (8)
- **MongoDB only**: reviews (5), promotions (6)
