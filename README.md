# useful-Astro-scripts
A dump of simple scripts I have quickly cooked up for particular problems I have faced. I am a pretty bad programmer and I bodge my way to making things work, trying to do better. 
This space will serve as a dump of solutions for seemingly trivial problems I have faced for my own future use and for anyone else who comes across similar problems. 

CSVtoVOtable.py: I used this to plot a
catalog of RGB stars used in https://www.aanda.org/articles/aa/pdf/2022/04/aa43307-22.pdf  (https://arxiv.org/abs/2204.03662)
on top of a HI moment 0 map, the catalog was in a csv file, but the visualisation software I used (CARTA https://cartavis.org/)
only takes VOtable inputs for catalogs 

cube_masking.py: A quick way to apply a binary value mask ( output of sofia-2 in my case https://gitlab.com/SoFiA-Admin/SoFiA-2) 
to a velocity cube. Takes a cube and a a mask fits file as input, saves the masked files
