use std::fs;
use std::io;

// Return a padded array of chars
fn parse(filename: &str) -> (Vec<Vec<char>>, usize) {
    let file_contents = fs::read_to_string(filename).unwrap();
    let lines = file_contents.split("\n");
    let mut ary = Vec::<Vec<char>>::new();

    let length = lines.clone().collect::<Vec<&str>>()[0].len() + 6;
    for _k in 0..3 {
        ary.push(Vec::<char>::new());
        for _i in 0..length {
            let idx = ary.len() - 1;
            ary[idx].push('.');
        }
    }

    for line in lines {
        ary.push(Vec::<char>::new());
        let idx = ary.len() - 1;
        for _k in 0..3 {
            ary[idx].push('.');
        }

        for ch in line.chars() {
            ary[idx].push(ch);
        }
        for _k in 0..3 {
            ary[idx].push('.');
        }
    }
    for _k in 0..3 {
        ary.push(Vec::<char>::new());
        for _i in 0..length {
            let idx = ary.len() - 1;
            ary[idx].push('.');
        }
    }
    return (ary, length);
}

fn test(
    ary: &Vec<Vec<char>>,
    i: i64,
    j: i64,
    iw: i64,
    jw: i64,
    ary2: &mut Vec<Vec<char>>,
) -> usize {
    // println!("i{} j{} iw {} jw{} eval {} , {}", i, j, iw, jw, );
    if ary[(i + (0 * iw)) as usize][(j + (0 * jw)) as usize] != 'X' {
        // println!("{} != X", ary[(i + (0 * iw)) as usize][(i + (0 * iw)) as usize]);
        return 0;
    }
    // print!("p!");
    if ary[(i + (1 * iw)) as usize][(j + (1 * jw)) as usize] != 'M' {
        return 0;
    }
    // print!("p!");
    if ary[(i + (2 * iw)) as usize][(j + (2 * jw)) as usize] != 'A' {
        return 0;
    }
    // print!("p!");
    if ary[(i + (3 * iw)) as usize][(j + (3 * jw)) as usize] != 'S' {
        return 0;
    }
    ary2[(i + (0 * iw)) as usize][(j + (0 * jw)) as usize] = '_';
    ary2[(i + (1 * iw)) as usize][(j + (1 * jw)) as usize] = '_';
    ary2[(i + (2 * iw)) as usize][(j + (2 * jw)) as usize] = '_';
    ary2[(i + (3 * iw)) as usize][(j + (3 * jw)) as usize] = '_';

    return 1;
}

fn check(ary: &Vec<Vec<char>>, i: i64, j: i64, ary2: &mut Vec<Vec<char>>) -> usize {
    return test(ary, i, j, 0, -1, ary2)
        + test(ary, i, j, 0, 1, ary2)
        + test(ary, i, j, -1, 0, ary2)
        + test(ary, i, j, 1, 0, ary2)
        + test(ary, i, j, 1, 1, ary2)
        + test(ary, i, j, -1, -1, ary2)
        + test(ary, i, j, 1, -1, ary2)
        + test(ary, i, j, -1, 1, ary2);
}

fn check_p2(ary: &Vec<Vec<char>>, i: i64, j: i64) -> usize {
    if ary[i as usize][j as usize] == 'S'
        && ary[(i + 2) as usize][j as usize] == 'M'
        && ary[(i + 1) as usize][(j + 1) as usize] == 'A'
        && ary[(i) as usize][(j + 2) as usize] == 'S'
        && ary[(i + 2) as usize][(j + 2) as usize] == 'M'
    {
        return 1;
    }

    if ary[i as usize][j as usize] == 'M'
        && ary[(i + 2) as usize][j as usize] == 'S'
        && ary[(i + 1) as usize][(j + 1) as usize] == 'A'
        && ary[(i) as usize][(j + 2) as usize] == 'M'
        && ary[(i + 2) as usize][(j + 2) as usize] == 'S'
    {
        return 1;
    }

    if ary[i as usize][j as usize] == 'S'
        && ary[(i + 2) as usize][j as usize] == 'S'
        && ary[(i + 1) as usize][(j + 1) as usize] == 'A'
        && ary[(i) as usize][(j + 2) as usize] == 'M'
        && ary[(i + 2) as usize][(j + 2) as usize] == 'M'
    {
        return 1;
    }

    if ary[i as usize][j as usize] == 'M'
        && ary[(i + 2) as usize][j as usize] == 'M'
        && ary[(i + 1) as usize][(j + 1) as usize] == 'A'
        && ary[(i) as usize][(j + 2) as usize] == 'S'
        && ary[(i + 2) as usize][(j + 2) as usize] == 'S'
    {
        return 1;
    }
    return 0;
}

fn main() -> io::Result<()> {
    let (ary, length) = parse("data");
    let mut total: usize = 0;
    let mut total_p2: usize = 0;
    let mut ary2 = ary.clone();

    for i in 3..ary.len() - 3 {
        for j in 3..length - 3 {
            total += check(
                &ary,
                i.try_into().unwrap(),
                j.try_into().unwrap(),
                &mut ary2,
            );
        }
    }

    for i in 3..ary.len() - 3 {
        for j in 3..length - 3 {
            total_p2 += check_p2(&ary, i.try_into().unwrap(), j.try_into().unwrap());
        }
    }
    println!("Answer Part 1: {}", total);
    println!("Answer Part 2: {}", total_p2);
    Ok(())
}
