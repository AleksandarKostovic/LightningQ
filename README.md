# LightningQ
LightningQ is a blueprint for design and manufacturing of Optical Quantum Computers.



## How to build

In order to build the GDS files yourself, you need [Nazca](https://nazca-design.org), Ipython and Pycliper python packages.

When those are installed, follow the following steps:
1. `cd LightningQ`
2. `make`
3. If you have layout viewer like Klayout, do `klayout nazca_export.gds`

For layout viewer it is reccomended to use Klayout.
