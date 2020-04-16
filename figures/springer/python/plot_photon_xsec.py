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

df_name = 'photon_xsec.csv'
df   = pd.read_csv(df_name)
# restore mass as column and sort 
#df = df.sort_values("mass_GeV")
#df.reset_index(inplace = True, drop = True)

df.columns = [col.strip() for col in df.columns]

plt.xscale("log")
plt.yscale("log")
#energy,coherent_scatter,incoherent_scatter,photoel_abs,nuclear_pair_prod ,electron_pair_prod,total
plt.plot(df.energy, df.total, label = r"Total", linestyle='dashed', linewidth=3)
plt.plot(df.energy, df.photoel_abs, label = r"Photoelectric effect")
plt.plot(df.energy, df.coherent_scatter, label = r"Rayleigh Scatter")
plt.plot(df.energy, df.incoherent_scatter, label = r"Compton scattering")
plt.plot(df.energy, df.nuclear_pair_prod, label = r"Nuclear Pair Prod.")
plt.plot(df.energy, df.electron_pair_prod, label = r"Electron Pair Prod.")



# draw legend and style plot
plt.xlabel("Photon Energy [MeV]")
plt.ylabel(r"Cross section [barns/atom]")
plt.grid()
#plt.xlim(200, 3000)
plt.ylim(1e-2, 1e7)
plt.legend(ncol = 2, framealpha = 1)
#plt.locator_params(axis = "y", base = 100) # for log-scaled axis, it's LogLocator, not MaxNLocator
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
plt.title(r"Photon interaction cross-section in lead (Z=82)", 
          fontsize = 9, loc = "center")
plt.savefig("../photon_xsec.pdf")
  
