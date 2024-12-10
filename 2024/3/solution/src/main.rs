use regex::Regex;
use std::fs;
use std::io;
use std::str::FromStr;

fn test_vec(s: &String) -> i64 {
    let mut result: i64 = 0;
    let re = Regex::new(r"mul\(([0-9]+),([0-9]+)\)").unwrap();

    let muls: Vec<(&str, &str)> = re
        .captures_iter(s)
        .map(|caps| {
            let (_, [vala, valb]) = caps.extract();
            (vala, valb)
        })
        .collect();
    for captures in muls {
        let (vala, valb) = captures;
        result += i64::from_str(vala).unwrap() * i64::from_str(valb).unwrap();
    }
    return result;
}

fn parse(filename: &str) -> Vec<String> {
    let file_contents = fs::read_to_string(filename).unwrap();
    let lines = file_contents.split("\n");
    let mut raw_strings = Vec::<String>::new();
    for line in lines {
        raw_strings.push(line.to_string());
    }
    return raw_strings;
}

fn main() -> io::Result<()> {
    let raw_strings: Vec<String> = parse("data");
    let mut total: i64 = 0;

    for string in raw_strings {
        total += test_vec(&string);
    }

    let mut total_p2: i64 = 0;

    println!("Answer Part 1: {}", total);
    println!("Answer Part 2: {}", total_p2 + total);

    Ok(())
}
