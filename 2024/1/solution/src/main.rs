use std::fs;
use std::io;
use std::str::FromStr;

fn main() -> io::Result<()> {
    let file_contents = fs::read_to_string("data")?;
    let lines = file_contents.split("\n");
    let mut a = Vec::<i64>::new();
    let mut b = Vec::<i64>::new();

    for line in lines {
        let avl = line.split("   ");
        let pair = avl.collect::<Vec<&str>>();

        if !pair.is_empty() && !pair[0].is_empty() && !pair[1].is_empty() {
            a.push(i64::from_str(pair[0]).unwrap());
            b.push(i64::from_str(pair[1]).unwrap());
        }
    }
    a.sort_unstable();
    b.sort_unstable();

    let mut total: i64 = 0;
    let mut sim: i64 = 0;
    for k in 0..a.len() {
        total += i64::abs(a[k] - b[k]);
        sim += a[k] *  (b.iter().filter(|&n| *n == a[k]).count() as i64);
    }
    println!("Answer Part 1: {}", total);
    println!("Answer Part 2: {}", sim);
    
    Ok(())
}
