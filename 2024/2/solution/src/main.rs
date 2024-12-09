use std::fs;
use std::io;
use std::str::FromStr;

fn test_vec(a: &Vec<i64>) -> (bool, usize) {
    let mut safe: bool = true;
    let inc: bool = a[0] < a[1];
    let mut fail: usize = 0;

    for l in 1..a.len() {
        if inc && (a[l] - a[l - 1] > 3 || a[l] - a[l - 1] <= 0) {
            safe = false;
            fail = l;
            break;
        }
        if !inc && (a[l - 1] - a[l] > 3 || a[l - 1] - a[l] <= 0) {
            safe = false;
            fail = l;
            break;
        }
    }
    if safe {
        return (true, 0);
    }
    return (false, fail);
}

fn main() -> io::Result<()> {
    let file_contents = fs::read_to_string("data")?;
    let lines = file_contents.split("\n");
    let mut a = Vec::<Vec<i64>>::new();

    for line in lines {
        let avl = line.split(" ");
        let pair = avl.collect::<Vec<&str>>();

        if !pair.is_empty() {
            let mut tmp = Vec::<i64>::new();
            for p in pair {
                tmp.push(i64::from_str(p).unwrap());
            }
            a.push(tmp);
        }
    }

    let mut total: i64 = 0;
    let mut total_p2: i64 = 0;

    for k in 0..a.len() {
        let (success, idx) = test_vec(&a[k]);

        if success {
            total += 1;
        } else {
            let mut final_succ = false;
            for i in 0..a[k].len() {
                let mut attempt1 = Vec::<i64>::new();
                for t in a[k]
                    .iter()
                    .enumerate()
                    .filter(|&(m, _)| m != i)
                    .map(|(_, e)| e)
                {
                    attempt1.push(*t);
                }
                if attempt1.len() > 1 {
                    let (success, _a1_idx) = test_vec(&attempt1);
                    if success {
                        final_succ = true;
                        break;
                    }
                }
            }
            if final_succ {
                total_p2 += 1;
            }
        }
    }
    println!("Answer Part 1: {}", total);
    println!("Answer Part 2: {}", total_p2 + total);

    Ok(())
}
