"""
Transforms and Loads data into the local SQLite3 database

"""
import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/airline-safety.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("AirlineSafetyDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS AirlineSafetyDB")
    c.execute(
        """
        CREATE TABLE AirlineSafetyDB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            airline TEXT,
            avail_seat_km_per_week INTEGER,
            incidents_85_99 INTEGER,
            fatal_accidents_85_99 INTEGER,
            fatalities_85_99 INTEGER,
            incidents_00_14 INTEGER,
            fatal_accidents_00_14 INTEGER,
            fatalities_00_14 INTEGER
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO AirlineSafetyDB(
            airline, 
            avail_seat_km_per_week,
            incidents_85_99, 
            fatal_accidents_85_99,
            fatalities_85_99,
            incidents_00_14,
            fatal_accidents_00_14,
            fatalities_00_14
            ) 
            VALUES (?,?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "ServeTimesDB.db"
