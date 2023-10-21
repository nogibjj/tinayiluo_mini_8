"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("AirlineSafetyDB.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
    airline,
    avail_seat_km_per_week,
    incidents_85_99,
    fatal_accidents_85_99,
    fatalities_85_99,
    incidents_00_14,
    fatal_accidents_00_14,
    fatalities_00_14,
):
    """create example query"""
    conn = sqlite3.connect("AirlineSafetyDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO AirlineSafetyDB
        (airline, 
        avail_seat_km_per_week, 
        incidents_85_99, 
        fatal_accidents_85_99, 
        fatalities_85_99,
        incidents_00_14,
        fatal_accidents_00_14, 
        fatalities_00_14) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            airline,
            avail_seat_km_per_week,
            incidents_85_99,
            fatal_accidents_85_99,
            fatalities_85_99,
            incidents_00_14,
            fatal_accidents_00_14,
            fatalities_00_14,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO AirlineSafetyDB VALUES (
            {airline}, 
            {avail_seat_km_per_week},
            {incidents_85_99}, 
            {fatal_accidents_85_99}, 
            {fatalities_85_99}, 
            {incidents_00_14}, 
            {fatal_accidents_00_14}, 
            {fatalities_00_14});"""
    )


def update_record(
    airline,
    avail_seat_km_per_week,
    incidents_85_99,
    fatal_accidents_85_99,
    fatalities_85_99,
    incidents_00_14,
    fatal_accidents_00_14,
    fatalities_00_14,
    record_id,
):
    """update example query"""
    conn = sqlite3.connect("AirlineSafetyDB.db")
    c = conn.cursor()
    print(
        (
            airline,
            avail_seat_km_per_week,
            incidents_85_99,
            fatal_accidents_85_99,
            fatalities_85_99,
            incidents_00_14,
            fatal_accidents_00_14,
            fatalities_00_14,
            record_id,
        )
    )
    c.execute(
        """
        UPDATE AirlineSafetyDB 
        SET airline=?,
        avail_seat_km_per_week=?, 
        incidents_85_99=?, 
        fatal_accidents_85_99=?, 
        fatalities_85_99=?, 
        incidents_00_14=?, 
        fatal_accidents_00_14=?, 
        fatalities_00_14=? 
        WHERE id=?;
        """,
        (
            airline,
            avail_seat_km_per_week,
            incidents_85_99,
            fatal_accidents_85_99,
            fatalities_85_99,
            incidents_00_14,
            fatal_accidents_00_14,
            fatalities_00_14,
            record_id,
        ),
    )

    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE AirlineSafetyDB SET 
        airline={airline}, 
        avail_seat_km_per_week={avail_seat_km_per_week},
        incidents_85_99=
        {incidents_85_99},
        fatal_accidents_85_99={fatal_accidents_85_99}, 
        fatalities_85_99={fatalities_85_99}, 
        incidents_00_14={incidents_00_14}, 
        fatal_accidents_00_14={fatal_accidents_00_14}, 
        fatalities_00_14={fatalities_00_14} 
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("AirlineSafetyDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM AirlineSafetyDB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM AirlineSafetyDB WHERE id={record_id};")


def read_data():
    """read data"""
    conn = sqlite3.connect("AirlineSafetyDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM AirlineSafetyDB")
    data = c.fetchall()
    log_query("SELECT * FROM AirlineSafetyDB;")
    return data
