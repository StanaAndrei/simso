# SimSo - Simulation of Multiprocessor Scheduling with Overheads

SimSo is a scheduling simulator for real-time multiprocessor architectures that takes into account some scheduling overheads (scheduling decisions, context switches) and the impact of caches through statistical models. Based on a Discrete-Event Simulator (SimPy), it allows quick simulations and a fast prototyping of scheduling policies using Python. Currently, [more than 25 popular schedulers are available](https://maximecheramy.github.io/simso/). 

## Documentation

You can access the documentation here: [Documentation of SimSo](https://maximecheramy.github.io/simso/). You will find tutorials that should help you to start.

## Download

SimSo is divided in 2 components: the core and the graphical user interface.

If you have Python installed (and PyQt4 for the GUI), you can install simso using the tool pip: pip install simso simsogui. This has the advantage to work on Linux, Mac OS and Windows.

The source code can also be found on PyPI and GitHub:

- SimSo (Python module): https://pypi.python.org/pypi/simso/
- Graphical User Interface: https://pypi.python.org/pypi/simsogui/

- SimSo (Python module): https://github.com/MaximeCheramy/simso
- Graphical User Interface: https://github.com/MaximeCheramy/simso-gui

You can also find a web version of SimSo here: https://maximecheramy.github.io/simso-web/ ([source](https://github.com/MaximeCheramy/simso-web)).

## Publications

The general presentation of the tool can be found in the following paper published at WATERS:

SimSo: A Simulation Tool to Evaluate Real-Time Multiprocessor Scheduling Algorithms. Maxime Chéramy, Pierre-Emmanuel Hladik and Anne-Marie Déplanche. In proceedings of the 5th International Workshop on Analysis Tools and Methodologies for Embedded and Real-time Systems (WATERS). July 2014.

How to cite:

```
@inproceedings{cheramy2014, Author = {Ch\'eramy, Maxime and Hladik, Pierre-Emmanuel and D\'eplanche, Anne-Marie}, Booktitle = {Proc. of the 5th International Workshop on Analysis Tools and Methodologies for Embedded and Real-time Systems}, Series = {WATERS}, Title = {SimSo: A Simulation Tool to Evaluate Real-Time Multiprocessor Scheduling Algorithms}, Year = {2014}}
```

## License

This is a free software available under the CeCILL license (GPL compatible).


## Contributions

Added a feature that enables you to create a custom task at runtime <br>
-This includes the creation of a custom task class with posibility to disable the fields you don't want/need. <br>
-The posibility to give it a custom name. <br>
-The posibility inject custom code to define the behaviour of the new task(or to keep the default code which generalizes the previous created task types). <br>

Added a feature that enables you to use what heuristic you want at runtime with P_EDF or P_RM schedulers. <br>
You can choose from: decreasing_worst_fit, decreasing_best_fit, decreasing_next_fit, decreasing_first_fit, first_fit, next_fit, worst_fit, best_fit
