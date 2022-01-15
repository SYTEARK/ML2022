#[macro_use]
extern crate peroxide;
use peroxide::fuga::*;

#[allow(non_snake_case)]
fn main() {
    let w1 = vec![1., 2., 3.];
    let w2 = w1.fmap(|t| t * -1f64);

    let x1 = seq(-2., 2., 0.01);
    let x2 = seq(-2, 2, 0.01);

    let X = feature_matrix(&x1, &x2);

    let c1 = h(&X, &w1);
    let c2 = h(&X, &w2);

    let g1 = X.add_col(&c1);
    let g2 = X.add_col(&c2);
        
    //let mut plt = Plot2D::new();
}

#[allow(non_snake_case)]
fn h(X: &Matrix, w: &Vec<f64>) -> Vec<f64> {
    (X * w).fmap(|t| t.signum())
}

fn feature_matrix(x1: &Vec<f64>, x2: &Vec<f64>) -> Matrix {
    let ones = vec![1.; x1.len()];
    hstack!(ones, x1, x2)
}
