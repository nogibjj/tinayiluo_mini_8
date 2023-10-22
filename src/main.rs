use std::env;
use std::fs::OpenOptions; // Added this import
use std::io::Write;
use std::time::Instant;
use tina_yi_sqlite::{extract, query, transform_load};

const LOG_FILE: &str = "rust_query_log.md"; // Define the LOG_FILE constant

fn log_query(action: &str, times: u128, mem_used: u64) -> std::io::Result<()> {
    let mut file = OpenOptions::new().append(true).create(true).open(LOG_FILE)?;

    writeln!(file, "```action\n{}\n```\n", action)?;
    writeln!(
        file,
        "The {} action took {} microseconds and used {} kB in Rust.\n",
        action, times, mem_used
    )?;

    Ok(())
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Usage: {} [action]", args[0]);
        return;
    }

    let action = &args[1];

    let start_time = Instant::now(); // Initialize start_time
                                     // Assuming you have the sys_info crate for mem_info.
    let mem_info_before = sys_info::mem_info().unwrap(); // Initialize mem_info_before

    match action.as_str() {
        "extract" => {
            extract(
                "https://github.com/fivethirtyeight/data/blob/master/airline-safety/airline-safety.csv?raw=true",
                "data/airline-safety.csv",
                "data",
            );
            let end_time = Instant::now();
            let elapsed_time = end_time.duration_since(start_time);
            let mem_info_after = sys_info::mem_info().unwrap();
            let mem_used = mem_info_after.total - mem_info_before.total;

            match log_query(action.as_str(), elapsed_time.as_micros(), mem_used) {
                // Removed borrowing
                Ok(_) => {}
                Err(e) => println!("Error: {:?}", e),
            }
        }
        "transform_load" => match transform_load("data/airline-safety.csv") {
            Ok(_) => println!("Data loaded successfully!"),
            Err(err) => eprintln!("Error: {:?}", err),
        },
        "query" => {
            if let Some(q) = args.get(2) {
                if let Err(err) = query(q) {
                    eprintln!("Error: {:?}", err);
                } else {
                    println!("Query executed successfully!");
                }
            } else {
                println!("Usage: {} query [SQL query]", args[0]);
            }
        }
        _ => {
            println!("Invalid action. Use 'extract', 'transform_load', or 'query'.");
        }
    }
}
