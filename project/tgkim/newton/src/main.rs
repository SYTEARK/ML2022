#[macro_use]
extern crate peroxide;
use peroxide::fuga::*;
use std::marker::PhantomData;

fn main() {
    let p = free_fall();

    let mut eom_solver = ExplicitODE::new(eom);

    let init_state: State<f64> = State::new(
        0f64,
        c!(20, 0),
        c!(0, -10)
    );

    eom_solver
        .set_initial_condition(init_state)
        .set_method(ExMethod::RK4)
        .set_step_size(1e-5)
        .set_times(1e+6 as usize)
        .set_env(p)
        .set_stop_condition(stop);

    let result = eom_solver.integrate();

    let mut df = DataFrame::new(vec![]);
    df.push("t", Series::new(result.col(0)));
    df.push("s", Series::new(result.col(1)));
    df.push("v", Series::new(result.col(2)));

    df.print();

    df.write_nc("data/free_fall.nc").expect("Can't write free_fall");
}

fn eom(st: &mut State<f64>, p: &Potential<AD>) {
    let xv = &st.value;
    let dxv = &mut st.deriv;

    let x_curr = xv[0];
    let v_curr = xv[1];

    let dvdx = p.call(AD1(x_curr, 1f64), xv).dx();

    dxv[0] = v_curr;    // dx/dt = v
    dxv[1] = -dvdx;     // dv/dt = a = F/m = -1/m * dV/dx
}

fn free_fall() -> Potential<AD> {
    Potential::new(vec![10f64], |x, p, _| x * p[0])
}

fn stop<E: Environment>(st: &ExplicitODE<E>) -> bool {
    let s = &st.get_state().value[0];
    *s <= 0f64
}

// =============================================================================
// Backend
// =============================================================================
pub struct Potential<T> where T: Real {
    params: Vec<f64>,
    f: Box<dyn Fn(T, &Vec<f64>, &Vec<f64>) -> T>,
    _t: PhantomData<T>
}

impl<T: Real> Potential<T> {
    fn new<F: Fn(T, &Vec<f64>, &Vec<f64>) -> T + 'static>(params: Vec<f64>, f: F) -> Self {
        Potential {
            params,
            f: Box::new(f),
            _t: PhantomData
        }
    }

    fn call(&self, x: T, st_value: &Vec<f64>) -> T {
        (self.f)(x, &self.params, st_value)
    }
}

impl Environment for Potential<f64> {}
impl Environment for Potential<AD> {}

impl Default for Potential<f64> {
    fn default() -> Self {
        Potential {
            params: vec![],
            f: Box::new(|_, _, _| 0f64),
            _t: PhantomData
        }
    }
}

impl Default for Potential<AD> {
    fn default() -> Self {
        Potential {
            params: vec![],
            f: Box::new(|_, _, _| AD0(0f64)),
            _t: PhantomData
        }
    }
}