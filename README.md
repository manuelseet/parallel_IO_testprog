# parallel_IO_testprog
Python test programme (psychopy) to test I/O via parallel port for TMS triggers [May 2017]. 

This Psychopy programme was developed to test the precision and synchrony of the Parallel Port component for use by an external transcranial magnetic stimulation system that 
delivers time-controlled ON-only triggers, as well as a third-party data acquisition hardware (PowerLab). 

Tested parameters include:
- stimulus onset asychrony (SOA) between a screen cue on the host computer and an Parallel Port event
- presence and absence of a trigger to the TMS event in the event

The data acquisition device is also calibrated, and should have an onset SOA = -0.05 relative to the main TMS trigger. 
Offset SOA = 0.30 relative to onset  

