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

import pandas as pd
import matplotlib.pyplot as plt


### helpers
def PlotXsec(df):
  plt.yscale("log")
  baseline = plt.plot(df.mass_GeV, df.xsec_pb, label = 'cross section')
  # check which uncertainty type we have
  if "unc_up_pb" in df.columns:
    # asymmetric
    band = plt.fill_between(df.mass_GeV, df.xsec_pb + df.unc_down_pb, df.xsec_pb + df.unc_up_pb, alpha = 0.2, facecolor = baseline[0].get_color(), linewidth=0)
  else:
    # assume symmetric always present
    band = plt.fill_between(df.mass_GeV, df.xsec_pb - df.unc_pb     , df.xsec_pb + df.unc_pb   , alpha = 0.2, facecolor = baseline[0].get_color(), linewidth=0, label='uncertainty')

  
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

df   = pd.read_csv('gluino_xsec_nlo.csv')
# restore mass as column and sort 
#df = df.sort_values("mass_GeV")
#df.reset_index(inplace = True, drop = True)

df.columns = [col.strip() for col in df.columns]
df['unc_pb'] = df['xsec_pb'] * df['100rel_unc'] / 100.
PlotXsec(df)

# plot


# draw legend and style plot
plt.xlabel("gluino mass [GeV]")
plt.ylabel("cross section [pb]")
plt.grid()
plt.xlim(200, 3000)
plt.ylim(1e-6, 1e4)
plt.legend(ncol = 2, framealpha = 1)
plt.locator_params(axis = "y", base = 100) # for log-scaled axis, it's LogLocator, not MaxNLocator
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
plt.title(r"LHC, $pp$, $\sqrt{s} = 13$ TeV, $\tilde{g}\tilde{g}$ production, NLO+NLL", fontsize = 9, loc = "right")
plt.savefig("../gluino_xsec.pdf")

