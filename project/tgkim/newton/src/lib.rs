use peroxide::fuga::*;
use std::marker::PhantomData;

// =============================================================================
// Potentials
// =============================================================================
pub fn free_fall() -> Potential<AD> {
    Potential::new(vec![10f64], |x, p, _| x * p[0])
}

pub fn drag_fall() -> Potential<AD> {
    Potential::new(
        vec![10f64, 0.1f64],
        |x, p, st| x * (p[0] - p[1] * st[1].powi(2))
    )
}

pub fn stop_fall<E: Environment>(st: &ExplicitODE<E>) -> bool {
    let s = &st.get_state().value[0];
    *s <= 0f64
}

pub fn sho() -> Potential<AD> {
    Potential::new(
        vec![10f64],
        |x: AD, p, _| 0.5 * p[0] * x.powi(2)
    )
}

pub fn sho_friction() -> Potential<AD> {
    Potential::new(
        vec![10f64, 0.3],
        |x: AD, p, st| 0.5 * p[0] * x.powi(2) + p[1] * 10f64 * st[1].signum() * x
    )
}

// =============================================================================
// Backend
// =============================================================================
pub fn eom(st: &mut State<f64>, p: &Potential<AD>) {
    let xv = &st.value;
    let dxv = &mut st.deriv;

    let x_curr = xv[0];
    let v_curr = xv[1];

    let dvdx = p.call(AD1(x_curr, 1f64), xv).dx();

    dxv[0] = v_curr;    // dx/dt = v
    dxv[1] = -dvdx;     // dv/dt = a = F/m = -1/m * dV/dx
}

pub struct Potential<T> where T: Real {
    pub params: Vec<f64>,
    f: Box<dyn Fn(T, &Vec<f64>, &Vec<f64>) -> T>,
    _t: PhantomData<T>
}

impl<T: Real> Potential<T> {
    pub fn new<F: Fn(T, &Vec<f64>, &Vec<f64>) -> T + 'static>(params: Vec<f64>, f: F) -> Self {
        Potential {
            params,
            f: Box::new(f),
            _t: PhantomData
        }
    }

    pub fn call(&self, x: T, st_value: &Vec<f64>) -> T {
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