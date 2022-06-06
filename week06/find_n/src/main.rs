#[macro_use]
extern crate peroxide;
use peroxide::fuga::*;

fn main() -> Result<(), RootError> {
    let root = newton(f_ad, 10000f64, 20usize, 1e-6)?;
    root.print();
    f(root.round() + 1f64).print();

    let root2 = newton(g_ad, 10000f64, 20usize, 1e-6)?;
    root2.print();
    g(root2.round()-1f64).print();
    Ok(())
}

#[ad_function]
fn f(N: f64) -> f64 {
    8f64 / 0.1.powi(2) * ((4f64 * (2f64 * N).powi(3) + 4f64) / 0.1).ln() - N
}

#[ad_function]
fn g(N: f64) -> f64 {
    N/3200f64 - ((4f64 * (2f64 * N).powi(10) + 4f64) / 0.05).ln()
}