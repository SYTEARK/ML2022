use peroxide::fuga::*;

const N: usize = 100_000;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut nu_1 = vec![0.0; N];
    let mut nu_rand = vec![0.0; N];
    let mut nu_min = vec![0.0; N];

    for i in 0 .. N {
        let (a, b, c) = experiment(10, 1000);
        nu_1[i] = a;
        nu_rand[i] = b;
        nu_min[i] = c;
    }

    let mut df = DataFrame::new(vec![]);
    df.push("nu_1",Series::new(nu_1));
    df.push("nu_rand",Series::new(nu_rand));
    df.push("nu_min",Series::new(nu_min));

    df.print();

    df.write_nc("data/ex_1_10.nc")?;

    Ok(())
}

#[derive(Debug, Copy, Clone, PartialEq, Eq)]
enum Coin {
    Head,
    Tail
}

impl Into<f64> for Coin {
    fn into(self) -> f64 {
        match self {
            Coin::Head => 1.0,
            Coin::Tail => 0.0
        }
    }
}

impl From<f64> for Coin {
    fn from(x: f64) -> Coin {
        if x == 1f64 {
            Coin::Head
        } else {
            Coin::Tail
        }
    }
}

impl Coin {
    fn new() -> Self {
        let bernoulli = Bernoulli(0.5);
        bernoulli.sample(1)[0].into()
    }

    fn flips(n: usize) -> Vec<Self> {
        let bernoulli = Bernoulli(0.5);
        bernoulli.sample(n).into_iter().map(|x| x.into()).collect()
    }
}

fn experiment(trial: usize, n: usize) -> (f64, f64, f64) {
    let mut heads = vec![0f64; n];
    for _ in 0 .. trial {
        let coins = Coin::flips(n);
        heads.mut_zip_with(
            |x, y| x + y,
            &coins.into_iter().map(|x| x.into()).collect()
        );
    }
    let nu_first = heads[0] / trial as f64;
    let rand_idx = Uniform(0i32, trial as i32).sample(1)[0] as usize;
    let nu_rand = heads[rand_idx] / trial as f64;
    let nu_min = heads.reduce(
        f64::MAX,
        |x, y| x.min(y)
    ) / trial as f64;
    
    (nu_first, nu_rand, nu_min)
}