use std::fs;
use std::io;
use std::str::FromStr;

fn parse(filename: &str) -> (Vec<Vec<usize>>, Vec<Vec<usize>>) {
    let file_contents = fs::read_to_string(filename).unwrap();
    let lines = file_contents.split("\n");
    let mut raw_strings = Vec::<Vec<usize>>::new();
    let mut rules = Vec::<Vec<usize>>::new();

    let mut mode: bool = false;
    for line in lines {
        if !mode {
            // Load rules
            if line.len() <= 1 {
                mode = true;
                continue;
            }
            rules.push(Vec::<usize>::new());
            let avl = line.split("|");
            let data = avl.collect::<Vec<&str>>();
            let idx = rules.len() - 1;
            for p in data {
                rules[idx].push(usize::from_str(p).unwrap());
            }
        } else {
            raw_strings.push(Vec::<usize>::new());
            let avl = line.split(",");
            let data = avl.collect::<Vec<&str>>();
            let idx = raw_strings.len() - 1;
            for p in data {
                raw_strings[idx].push(usize::from_str(p).unwrap());
            }
        }
    }
    return (rules, raw_strings);
}

fn p1(rules: &Vec<Vec<usize>>, pages: &Vec<usize>) -> usize {
    for (idx, page) in pages.iter().enumerate() {
        for rule in rules {
            if *page == rule[0] {
                for i in 0..idx {
                    if pages[i] == rule[1] {
                        return 0;
                    }
                }
            }

            if *page == rule[1] {
                for i in idx..pages.len() {
                    if pages[i] == rule[0] {
                        return 0;
                    }
                }
            }
        }
    }
    return pages[pages.len() / 2];
}

fn main() -> io::Result<()> {
    let (rules, raw_strings) = parse("data");
    let mut total: usize = 0;
    let mut total_p2: usize = 0;

    for pages in raw_strings {
        total += p1(&rules, &pages);
    }

    println!("Answer Part 1: {}", total);
    println!("Answer Part 2: {}", total_p2);

    Ok(())
}
