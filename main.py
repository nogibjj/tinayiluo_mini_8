"""handles cli commands"""
import sys
import os
import argparse
import time
import psutil
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    update_record,
    delete_record,
    create_record,
    general_query,
    read_data,
)

LOG_FILE = "python_query_log.md"


def log_query(action, times, mem_used):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```action\n{action}\n```\n\n")
        file.write(
            f"The {action} action took {times} microseconds in Python.\n"
            f"The {action} action used {mem_used} kB in Python.\n"
        )


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_record",
            "delete_record",
            "create_record",
            "general_query",
            "read_data",
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)
    if args.action == "update_record":
        parser.add_argument("airline")
        parser.add_argument("avail_seat_km_per_week", type=int)
        parser.add_argument("incidents_85_99", type=int)
        parser.add_argument("fatal_accidents_85_99", type=int)
        parser.add_argument("fatalities_85_99", type=int)
        parser.add_argument("incidents_00_14", type=int)
        parser.add_argument("fatal_accidents_00_14", type=int)
        parser.add_argument("fatalities_00_14", type=int)
        parser.add_argument("record_id", type=int)

    if args.action == "create_record":
        parser.add_argument("airline")
        parser.add_argument("avail_seat_km_per_week", type=int)
        parser.add_argument("incidents_85_99", type=int)
        parser.add_argument("fatal_accidents_85_99", type=int)
        parser.add_argument("fatalities_85_99", type=int)
        parser.add_argument("incidents_00_14", type=int)
        parser.add_argument("fatal_accidents_00_14", type=int)
        parser.add_argument("fatalities_00_14", type=int)

    if args.action == "general_query":
        parser.add_argument("query")

    if args.action == "delete_record":
        parser.add_argument("record_id", type=int)

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    start_time = time.perf_counter()
    memory_before = psutil.Process(os.getpid()).memory_info().rss / 1024

    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
        end_time = time.perf_counter()
        elapsed_time_micros = (end_time - start_time) * 1e6
        memory_after = psutil.Process(os.getpid()).memory_info().rss / 1024
        memory_used = memory_after - memory_before
        print(memory_used)

        log_query(
            args.action,
            elapsed_time_micros,
            memory_used,
        )
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "update_record":
        print(args)
        update_record(
            args.airline,
            args.avail_seat_km_per_week,
            args.incidents_85_99,
            args.fatal_accidents_85_99,
            args.fatalities_85_99,
            args.incidents_00_14,
            args.fatal_accidents_00_14,
            args.fatalities_00_14,
            args.record_id,
        )
    elif args.action == "delete_record":
        delete_record(args.record_id)
    elif args.action == "create_record":
        create_record(
            args.airline,
            args.avail_seat_km_per_week,
            args.incidents_85_99,
            args.fatal_accidents_85_99,
            args.fatalities_85_99,
            args.incidents_00_14,
            args.fatal_accidents_00_14,
            args.fatalities_00_14,
        )
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_data":
        data = read_data()
        print(data)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
