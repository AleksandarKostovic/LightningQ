# LightningQ
LightningQ is a blueprint for design and manufacturing of Optical Quantum Computers.

## How to build

In order to build the GDS files yourself, you need [Nazca](https://nazca-design.org), Ipython and Pycliper Python 3 packages.

When those are installed, follow the following steps:
1. `git clone https://github.com/AleksandarKostovic/LightningQ`
2. `cd LightningQ`
3. `make`
4. If you have layout viewer like Klayout, do `klayout nazca_export.gds`

For layout viewer it is reccomended to use Klayout.

## Contributing

If you would like to contribute to the project, please start a pull request with your improvements. Help is very much wanted especially with documentation, which will come soon.
