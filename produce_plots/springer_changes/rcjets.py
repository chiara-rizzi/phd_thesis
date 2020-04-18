import uproot 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch

f_name = '../root/mc16_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_TOPQ1.e6337_s3126_r9364_p3832.root'
tree_name = 'nominal'

file = uproot.open(f_name)
tree = file[tree_name]
df1 = tree.pandas.df(['event_number','run_number',
                      'jets_n','rc_RCJ_r10pt05_jets_n','ak10_jets_n', 
                      'rc_RCJ_r10pt05_jets_nconst',

                      'ak10_jets_pt','ak10_jets_phi','ak10_jets_eta',
                      'rc_RCJ_r10pt05_jets_pt','rc_RCJ_r10pt05_jets_phi','rc_RCJ_r10pt05_jets_eta',
                      'jets_pt','jets_phi','jets_eta'
                      ],flatten=False)
for index, row in df1.iterrows():
    if row['jets_n'] >=10 and row['rc_RCJ_r10pt05_jets_n']>=2 and row['rc_RCJ_r10pt05_jets_n'] >3:
        has_many_const = False
        for i in row['rc_RCJ_r10pt05_jets_nconst']:
            if i >= 3:
                has_many_const = True                
        if has_many_const:
            fig = plt.figure()
            ax = fig.add_subplot()
            print(row['jets_eta'],'\n', row['jets_phi'])
            for i,eta in enumerate(row['ak10_jets_eta']):
                phi = row['ak10_jets_phi'][i]                
                ax.add_patch(Circle((eta,phi), radius=1.0, color='blue', alpha=0.2))
            for i,eta in enumerate(row['jets_eta'][:-1]):
                phi = row['jets_phi'][i]                
                ax.add_patch(Circle((eta,phi), radius=0.4, color='red', alpha=0.2))
            ax.plot(row['jets_eta'][:-1], row['jets_phi'][:-1], 'o', color='red', label='anti-kt R=0.4 jets')
            ax.plot(row['rc_RCJ_r10pt05_jets_eta'], row['rc_RCJ_r10pt05_jets_phi'], '*', markersize=15, color='green', label='Reclustered jets')
            ax.plot(row['ak10_jets_eta'], row['ak10_jets_phi'], 'o', color='blue', label='anti-kt R=1.0 jets')
            ax.set_xlim([-3.5,3.5])
            ax.set_ylim([-3.5,3.5])
            ax.set_aspect(1.0/ax.get_data_ratio()*1.0)
            plt.legend(loc='best', shadow=False, fontsize='large')
            plt.xlabel(r"$\eta$", fontsize='large')
            plt.ylabel(r"$\phi$", fontsize='large')
            plt.title(r"C. Rizzi PhD Thesis                 $t\bar{t}$, $\sqrt{s}$=13TeV")
            plt.grid(True)
            plt.savefig('../'+str(row['run_number'])+'_'+str(row['event_number'])+'.pdf')
            plt.close()
            break
