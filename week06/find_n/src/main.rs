#[macro_use]
extern crate peroxide;
use peroxide::fuga::*;

fn main() -> Result<(), RootError> {
    let root = newton(f_ad, 10000f64, 20usize, 1e-6)?;
    root.print();
    f(root.round() + 1f64).print();
    Ok(())
}

#[ad_function]
fn f(N: f64) -> f64 {
    8f64 / 0.1.powi(2) * ((4f64 * (2f64 * N).powi(3) + 4f64) / 0.1).ln() - N
}