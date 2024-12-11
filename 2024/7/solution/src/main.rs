use std::fs;
use std::io;
use std::str::FromStr;

// Return a padded array of chars
fn parse(filename: &str) -> (Vec<usize>, Vec<Vec<usize>>) {
    let file_contents = fs::read_to_string(filename).unwrap();
    let lines = file_contents.split("\n");
    let mut a = Vec::<usize>::new();
    let mut b = Vec::<Vec<usize>>::new();

    for line in lines {
        let pair = line.split(":").collect::<Vec<&str>>();
        if !pair.is_empty() && !pair[0].is_empty() && !pair[1].is_empty() {
            a.push(usize::from_str(pair[0]).unwrap());
            let operands = pair[1].trim().split(" ").collect::<Vec<&str>>();
            b.push(Vec::<usize>::new());
            for operand in operands {
                let idx = b.len() - 1;
                b[idx].push(usize::from_str(operand).unwrap());
            }
        }
    }
    return (a, b);
}

fn combine(operands: &Vec<usize>) -> Vec<usize> {
    let mut result = Vec::<usize>::new();
    result.push(operands[0]);
    let mut ptr = 0;
    for i in 1..operands.len() {
        let imm_result = result.clone();
        for j in ptr..imm_result.len() {
            // Retain multiply result for all
            result.push(imm_result[j] * operands[i]);

            // Retain add result for all
            result.push(imm_result[j] + operands[i]);

            // Walk the pointer forward to ignore consumed values in the future.
            ptr += 1;
        }
    }
    let result2 = &result[ptr..result.len()];
    return result2.to_vec();
}

fn combine_p2(operands: &Vec<usize>) -> Vec<usize> {
    let mut result = Vec::<usize>::new();
    result.push(operands[0]);
    let mut ptr = 0;
    for i in 1..operands.len() {
        let imm_result = result.clone();
        for j in ptr..imm_result.len() {
            result.push(imm_result[j] * operands[i]); // Mult op
            result.push(imm_result[j] + operands[i]); // Add Op

            // Concat Op
            let mut a = imm_result[j].to_string().to_owned();
            let b = operands[i].to_string().to_owned();
            a.push_str(b.as_str());
            result.push(usize::from_str(a.as_str()).unwrap());

            // Pointer walk
            ptr += 1;
        }
    }
    let result2 = &result[ptr..result.len()];
    return result2.to_vec();
}

fn main() -> io::Result<()> {
    let filen = "data";
    let (mut expected, operands) = parse(filen);

    let mut total_p1 = 0;
    let mut total_p2 = 0;

    for i in 0..expected.len() {
        let data = combine(&operands[i]);
        for d in data {
            if d == expected[i] {
                total_p1 += expected[i];
                break;
            }
        }
    }

    for i in 0..expected.len() {
        let data = combine_p2(&operands[i]);
        for d in data {
            if d == expected[i] {
                total_p2 += expected[i];
                break;
            }
        }
    }

    println!("Answer Part 1: {}", total_p1);
    println!("Answer Part 2: {}", total_p2);
    Ok(())
}
