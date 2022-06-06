# RNN with Newton Equation of Motion

## Description

1. Data generation from solving ODE by [Peroxide](https://github.com/Axect/Peroxide)
2. Learning network via [PyTorch](https://pytorch.org/)

## Data Download

### Pre requisites

* [gdown](https://github.com/wkentaro/gdown)

### Download

1. Linux
    ```sh
    sh download.sh
    ```

2. Windows
    1. Download via gdown
        ```sh
        gdown --id 1VBWG8Fp-_49C-7oXMc5RXa52ekSk-VJ-
        ```
    
    2. Unzip

    3. Remove the zip file

## Notebooks

* RK4 : Runge-Kutta 4th order
* GL4 : Gauss-Legendre 4th order

### SHO

* LSTM
    * [LSTM with only $x$ (RK4)](./notebooks/NewtonRNN%20(PyTorch%20-%20SHO).ipynb)

### SHO with Friction

1. MLP
    * [MLP with only $x$ (RK4)](./notebooks/NewtonMLP%20(PyTorch%20-%20SHOF).ipynb)
    * [MLP with $(x, v)$ (RK4)](./notebooks/NewtonMLP%20(PyTorch%20-%20SHOFv2).ipynb)
    * [MLP with $(x, v)$ (GL4)](./notebooks/NewtonMLP%20(PyTorch%20-%20SHOFv2%20-%20GL4).ipynb)

2. LSTM
    * [LSTM with only $x$ (RK4)](./notebooks/NewtonRNN%20(PyTorch%20-%20SHOF).ipynb)
    * [LSTM with $(x,v)$ (GL4)](./notebooks/NewtonRNN%20(PyTorch%20-%20SHOFv2%20-%20GL4).ipynb)
    * [LSTM(4-layers) with $(x,v)$ (GL4)](./notebooks/NewtonRNN%20(PyTorch%20-%20SHOF%20-%20GL4%20-%20LSTM4).ipynb)

3. GRU
    * [GRU with $(x,v)$ (GL4)](./notebooks/NewtonRNN%20(PyTorch%20-%20SHOF%20-%20GL4%20-%20GRU).ipynb)
    * [GRU(4-layers) with $(x,v)$ (GL4)](./notebooks/NewtonRNN%20(PyTorch%20-%20SHOF%20-%20GL4%20-%20GRU4).ipynb)