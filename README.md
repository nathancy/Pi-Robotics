# Pi-LIDAR-Blockchain

Python code used to run an autonomous robot built using Arduino, Raspberry Pi, and LIDAR, and blockchain technology

Run with program with:
```
python main.py
```

The robot initially turns the LIDAR to the left, right, and center to calibrate by taking 5 readings, removes outliers and returns a median value. It then moves in the direction of the farthest distance. THe robot takes readings while in motion. If it encounters an obstacle, it stops and calibrates again to determine the next direction. 
