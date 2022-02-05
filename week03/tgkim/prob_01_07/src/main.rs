use peroxide::fuga::*;

#[allow(non_snake_case)]
fn main() -> Result<(), Box<dyn Error>>{
    let N = 6;
    let mu = 0.5;
    let m = 2;

    let epsilon = seq(0.0, 0.5, 0.01);
    let f = |eps: f64| {
        (0 .. 100_000)
            .into_iter()
            .map(|_| experiment(N, mu, m))
            .fold(
                0f64,
                |acc, x | {
                    if x > eps {
                        acc + 1f64
                    } else {
                        acc
                    }
                }
            ) / 100_000f64
    };
    let g = |eps: f64| hoeffding_bound(N, m, eps);
    let result = epsilon.fmap(f);
    let bound = epsilon.fmap(g);

    let mut df = DataFrame::new(vec![]);
    df.push("epsilon", Series::new(epsilon));
    df.push("result", Series::new(result));
    df.push("bound", Series::new(bound));

    df.print();

    df.write_nc("data/prob_01_07.nc")?;
    Ok(())
}

#[allow(non_snake_case)]
fn experiment(N: usize, mu: f64, m: usize) -> f64 {
    let binom = Binomial(N, mu);
    binom.sample(m).into_iter()
        .map(|x| x / N as f64)
        .map(|nu| (nu - mu).abs())
        .fold(f64::MIN, |x, y| x.max(y))
}

fn hoeffding_bound(N: usize, m: usize, epsilon: f64) -> f64 {
    2f64 * (m as f64) * (-2f64 * N as f64 * epsilon.powi(2)).exp()
}