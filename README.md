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

If you would like to contribute to the project, please start a pull request with your improvements. I would be interested to see the changes.

## Adding more Qubits

Here, in the existing code you can build a system for four qubits, however, you can do it as much as you like, where you could for example have 5, 6, 7 or more. Its up to you.

For adding more qubits, simply add these lines before `nd.export_gds()` function:

```python
qubit.put(0, -2080)
```
As Nazca uses X and Y axes to define position for items, you can add Qubit by just adding 520 to the `-2080` number, with each qubit added. So you end up with `-2600` for next position. As long as you keep adding 520 to teh negatie number, number of Qubits will rise(you have to call a qubit.put function of course, every time you want to add a Qubit). For more info about numbering system in Nazca, please consult this [excellent online manual](https://nazca-design.org/manual/getting_started.html).

## Documentation

Please see `doc` directory, where you will find a paper that explains how the idea came to be and how it works.
