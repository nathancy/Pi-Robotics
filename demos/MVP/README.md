# Demos

Set of demos to demonstrate two realistic scenarios.

```
Car #1 <- Car #2

Two cars following each other

Scenario #1: Car #1 is trustworthy
             Car #1 sends stop signal to car #2
             Car #2 stops
             Both cars stop
              
Scenario #2: Car #1 is not trustworthy
             Car #1 sends stop signal to car #2
             Car #2 continues on since car #1 is not trusted
             Both keep going forward
```

This repository contains several files:

* `car1_coord.py` - Script for Car #1 with Coordinator XBee attached
* `car2_router.py` - Script for Car #2 with Router XBee attached

Run the test module by running the scripts in a separate terminal:

Usage: python car1_coord.py [options]

Mode options: `1` (Scenario #1) or `2` (Scenario #2)

```
python car1_coord.py [options]
```

and

```
python car2_router.py [options]
```


