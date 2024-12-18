use std::fs;
use std::io;

// Return a padded array of chars
fn parse(filename: &str) -> (Vec<Vec<char>>, usize) {
    let file_contents = fs::read_to_string(filename).unwrap();
    let lines = file_contents.split("\n");
    let mut ary = Vec::<Vec<char>>::new();

    let length = lines.clone().collect::<Vec<&str>>()[0].len() + 6;
    for _k in 0..1 {
        ary.push(Vec::<char>::new());
        for _i in 0..length {
            // Pad the array so we don't ever have to think about bounds.
            let idx = ary.len() - 1;
            ary[idx].push('!');
        }
    }

    for line in lines {
        ary.push(Vec::<char>::new());
        let idx = ary.len() - 1;
        for _k in 0..1 {
            // Pad the array so we don't ever have to think about bounds.
            ary[idx].push('!');
        }

        for ch in line.chars() {
            // Push actual char.
            ary[idx].push(ch);
        }
        for _k in 0.. 1{
            // Pad the array so we don't ever have to think about bounds.
            ary[idx].push('!');
        }
    }

    for _k in 0..1 {
        ary.push(Vec::<char>::new());
        for _i in 0..length {
            // Pad the array so we don't ever have to think about bounds.
            let idx = ary.len() - 1;
            ary[idx].push('!');
        }
    }
    return (ary, length);
}

fn turn(id: i64, jd: i64) -> (i64, i64) {
    if id == 0 && jd == 1 {
        // right
        return (1,0);
    }
    if id == 1 && jd == 0 {
        // down
        return (0, -1);
    }
    if id == 0 && jd == -1 {
        // left
        return (-1, 0);
    }
    if id == -1 && jd == 0 {
        // up
        return (0,1);
    }
    return (15000,15000);
}

fn adv(ary: &mut Vec<Vec<char>>, i: i64, j: i64, mut id: i64, mut jd:i64) -> (i64, i64, i64, i64, bool) {

    if ary[(i + id) as usize][(j + jd) as usize] == '!' { ary[i as usize][j as usize] = 'X';return (0, 0, 0, 0, true);}
    if ary[(i + id) as usize][(j + jd) as usize] == '#' {
        (id, jd) = turn(id, jd);
        return (i, j, id, jd, false);
    }
    ary[i as usize][j as usize] = 'X';
    return (i + id, j + jd, id, jd, false);
}

fn main() -> io::Result<()> {
    let filen = "data";
    let (mut ary, _) = parse(filen);
    let mut total: usize = 0;
    
    let mut total_p2: usize = 0;

    let mut i:i64 = 0;
    let mut j:i64 = 0;
    let mut id:i64 = -1;
    let mut jd:i64 = 0;
    let mut done:bool = false;

    // Part 1
    for ik in 1..ary.len() - 1 {
        for jk in 1..ary[ik as usize].len() - 1 {
            if ary[ik as usize][jk as usize] == '^' {
                i = ik as i64;
                j = jk as i64;
                break;
            }
        }
    }

    let imm: i64 = i;
    let jmm: i64 = j;

    while !done {
        (i, j, id, jd, done) = adv(&mut ary, i, j, id, jd);
    }

    for ik in 1..ary.len() - 1 {
        for jk in 1..ary[ik as usize].len() - 1 {
            if ary[ik as usize][jk as usize] == 'X' {
                total += 1;
            }
        }
    }
        let (ary3,_) = parse(filen);

        // Part 2
        for ik in 1..ary3.len() - 1 {
            println!("Test Row {}", ik);
            for jk in 1..(ary3[ik as usize].len() - 1) {

                let mut ary2 = ary3.clone();
                i = imm;
                j = jmm;
                let mut id:i64 = -1;
                let mut jd:i64 = 0;

                ary2[ik as usize][jk as usize] = '#';

                // Truly sad way to figure out if we are stuck. If we have run enough rounds to have visited every cell, probably stuck. :-(
                let stuck:  usize = ary2.len() * ary2.len(); 
                let mut done: bool = false;
                let mut count: usize =0;
                while !done {
                    count += 1;
                    (i, j, id, jd, done) = adv(&mut ary2, i, j, id, jd);
                    if count >= stuck {
                        total_p2 += 1;
                        break;
                    }
                }

           }
        }

    println!("Answer Part 1: {}", total);
    println!("Answer Part 2: {}", total_p2);
    Ok(())
}
