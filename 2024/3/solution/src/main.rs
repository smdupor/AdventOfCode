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

fn test_vec_part2(s: &String) -> i64 {
    let mut result: i64 = 0;

    // Find enabled ranges
    let re = Regex::new(r"do\(\).*?().*?don't\(\)").unwrap();

    // Find values in an enabled range
    let re2 = Regex::new(r"mul\(([0-9]+),([0-9]+)\)").unwrap();

    for mat in re.find_iter(s) {
        let mul_args: Vec<(&str, &str)> = re2
            .captures_iter(&s[mat.start()..mat.end()])
            .map(|caps| {
                let (_, [vala, valb]) = caps.extract();
                (vala, valb)
            })
            .collect();
        for captures in mul_args {
            let (vala, valb) = captures;
            result += i64::from_str(vala).unwrap() * i64::from_str(valb).unwrap();
        }
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

    let mut total_p2: i64 = 0;
    let mut glob = String::new();

    // Part 2: Mult is enabled at start of string.
    glob += "do()";
    for string in raw_strings {
        total += test_vec(&string);
        glob += &string; // Part 2: Glob everything into one long string.
    }

    // Part 2: Regex cannot handle unterminated string. Terminate it with a don't().
    glob += "don't()";

    total_p2 += test_vec_part2(&glob);

    println!("Answer Part 1: {}", total);
    println!("Answer Part 2: {}", total_p2);

    Ok(())
}
