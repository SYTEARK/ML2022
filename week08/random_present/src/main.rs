use peroxide::fuga::*;

fn main() {
    //let a = vec!["태근", "예지", "동훈", "수진", "진흥", "상호"];
    let a = vec!["태근", "예지", "동훈", "수진", "진흥"];
    
    let u = Uniform(0, 4);
    let idx = u.sample(1)[0];

    println!("당첨된 발표자는 {}님 입니다.", a[idx as usize]);
}
