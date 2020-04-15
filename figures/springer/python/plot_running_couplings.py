#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Example script to create 1-D plots of cross sections as function of mass from data in JSON format.
# 
# External requirements (Python modules):
# 
#   pandas (https://pandas.pydata.org/)
#   matplotlib (https://matplotlib.org/)
# 
# Run with:
# 
#   python plot_xsecs_from_json.py
# 
# (85) 
#
# $Id: plot_xsecs_from_json.py 3190 2019-05-28 17:21:31Z eis $



### imports
import os
import json
import math
import pandas as pd
import matplotlib.pyplot as plt
  
### main

# init plotting
plt.ion()
use_latex = False
if use_latex:
  plt.rc('text', usetex=True)
  plt.rc('font', size=18)
  plt.rc('legend', fontsize=14)
  plt.rc('text.latex', preamble=r'\usepackage{cmbright}')
else:
  plt.rcParams.update({'font.size': 10})

df   = pd.read_csv('alpha.csv')
# restore mass as column and sort 
#df = df.sort_values("mass_GeV")
#df.reset_index(inplace = True, drop = True)

df.columns = [col.strip() for col in df.columns]

plt.xscale("log")
df['pl1']= 4*math.pi/(df['g1']*df['g1'])
df['pl2']= 4*math.pi/(df['g2']*df['g2'])
df['pl3']= 4*math.pi/(df['g3']*df['g3'])
plt.plot(df.Q, df.pl1, label = r"$\alpha_{1}$")
plt.plot(df.Q, df.pl2, label = r"$\alpha_{2}$")
plt.plot(df.Q, df.pl3, label = r"$\alpha_{3}$")


# plot


# draw legend and style plot
plt.xlabel("Q [GeV]")
plt.ylabel(r"$\alpha^{-1}$")
plt.grid()
#plt.xlim(200, 3000)
#plt.ylim(1e-6, 1e4)
plt.legend(ncol = 3, framealpha = 1)
#plt.locator_params(axis = "y", base = 100) # for log-scaled axis, it's LogLocator, not MaxNLocator
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
plt.title(r"C. Rizzi PhD Thesis               SOFTSUSY4.1.9, M$_{0}$=M$_{12}=2 TeV, A$_{0}$=0$, tan$\beta$=30", 
          fontsize = 9, loc = "right")
plt.savefig("coupling_constants.pdf")

