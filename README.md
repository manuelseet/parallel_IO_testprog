# parallel_IO_testprog
Python test programme (psychopy) to test I/O via parallel port for TMS triggers [May 2017]. 
-- Script developed to support my Honours Year empirical reserch project
-- Final project was peer-reviewed and published in an international neuroscience journal (Seet, Livesey & Harris, 2019)




This Psychopy programme was developed to test the precision and synchrony of the Parallel Port component for use by an external transcranial magnetic stimulation system that 
delivers time-controlled ON-only triggers, as well as a third-party data acquisition hardware (PowerLab). 

Tested parameters include:
- stimulus onset asychrony (SOA) between a screen cue on the host computer and an Parallel Port event
- presence and absence of a trigger to the TMS event in the event

The data acquisition device is also calibrated, and should have an onset SOA = -0.05 relative to the main TMS trigger. 
Offset SOA = 0.30 relative to onset  

REFERENCES

Seet, M. S., Livesey, E. J., & Harris, J. A. (2019). Associatively-mediated suppression of corticospinal excitability: A transcranial magnetic stimulation (TMS) study. Neuroscience, 416, 1-8. Link: https://www.sciencedirect.com/science/article/abs/pii/S0306452219305226
