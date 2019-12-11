use std::io::{self, Read};

fn main() -> Result<(), io::Error> {
    let mut buf = String::new();
    std::io::stdin().read_to_string(&mut buf)?;
    let mut numbers: Vec<i64> = buf
        .split_whitespace()
        .map(|s| s.parse::<i64>().unwrap())
        .skip(1)
        .collect();
    numbers.sort();
    numbers.reverse();
    let longest = numbers
        .iter()
        .enumerate()
        .map(|(idx, &item)| 1 + idx as i64 + item)
        .max_by_key(|x| *x)
        .unwrap();
    println!("{}", 1 + longest);
    Ok(())
}
