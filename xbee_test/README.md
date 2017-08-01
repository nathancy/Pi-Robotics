# XBee module 

Isolated XBee module for sending and receiving packets between two remote XBees.

This repository contains several files:
* `xbeeControl.py` - Main XBee control class 
* `receive_xbee.py` - XBee test driver to continuously read the serial port and process data
* `send_xbee.py` - XBee test driver to continuously send packets to a remote XBee 
* `xbee_test_driver.py` - XBee test driver that uses the class to send or receive packets 

Run the test driver with:
```
python xbee_test_driver.py
```

