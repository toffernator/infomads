# INFOMADS

The repository consists of two parts:
1. A tool for generating feasible instances of the _Strike!_ problem.
2. A tool that implements 4 algorithms (1 offline algorithm and 3 online algorithms) showing the average competitive-ratio of those four algorithms given a any number of instances.

Both parts are developed using [Python 3.11](https://www.python.org/downloads/release/python-3110/), and it is assumed you have a working installation of Python 3.11.
Moreover, part (2) uses [matplotlib](https://pypi.org/project/matplotlib/) to generate the graph of the results.

## Generating Instances

Run this tool using `python3`:

```sh
python3 generator.py
```

This will generate the `instances/` folder containing a bunch of randomly generated instances (which are guarantueed to be feasible)

## Average Competitive Ratio of Algorithms

To compute the average competitive ratio of the implemented algorithms you can run `main.py` passing either a single `.in` or a folder container many `.in` files as a command-line argument:

```sh
python3 main.py instances
```

or, for a single file:

```sh
python3 main.yp instances/n-28-m-6-4.in
```
