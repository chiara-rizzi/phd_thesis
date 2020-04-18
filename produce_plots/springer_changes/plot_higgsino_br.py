import math 
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-m1', default=500, type=float, help='M1')
parser.add_argument('-m2', default=1000, type=float, help='M2')
parser.add_argument('-eta', default=1.0, type=float, help='eta')
parser.add_argument('-tanb', default=20.0, type=float, help='tanBeta')
args = parser.parse_args()

plt.rcParams.update({'font.size': 11})

mZ = 80.4
mh = 125

s2w = 0.23120
sw = math.sqrt(s2w) 
w = math.asin(sw)
cw = math.cos(w)
c2w = cw*cw

beta = math.atan(args.tanb)
sb = math.sin(beta)
cb = math.cos(beta)

def BRh (mchi):
    if mchi < mh: 
        return 0
    first = (1./4)*math.pow((sb - args.eta*cb),2)
    second = math.pow( 1 - math.pow(mh/mchi,2), 4)
    return first*second

def BRZ (mchi):
    if mchi < mZ:
        return 0
    first = (1./4)*math.pow((sb + args.eta*cb),2)
    second = math.pow( 1 - math.pow(mZ/mchi,2), 4)
    return first*second

def BRy (mchi):
    first = (1./2)*math.pow((sb + args.eta*cb),2)
    second = math.pow(cw*sw*(args.m1 - args.m2)*mZ/(args.m1*args.m2) , 2)
    return first*second

x=[]
pl1=[]
pl2=[]
pl3=[]
for mchi in range(100,900):
    x.append(mchi)
    pl1.append(BRh(mchi))
    pl2.append(BRZ(mchi))
    pl3.append(BRy(mchi))

for i in range(0,len(pl1)):
    sum = pl1[i] + pl2[i] + pl3[i]
    pl1[i] = pl1[i]/sum
    pl2[i] = pl2[i]/sum
    pl3[i] = pl3[i]/sum

plt.plot(x, pl1, label = r"BR(h)")
plt.plot(x, pl2, label = r"BR(Z)")
plt.plot(x, pl3, label = r"BR($\gamma$)")
# draw legend and style plot
plt.xlabel(r"m($\tilde{\chi}_{1}^{0}$) [GeV]")
plt.ylabel(r"BR")
plt.grid()
#plt.xlim(200, 3000)
#plt.ylim(1e-6, 1e4)
plt.legend(ncol = 3, framealpha = 1)
#plt.locator_params(axis = "y", base = 100) # for log-scaled axis, it's LogLocator, not MaxNLocator
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
#plt.title(r"C. Rizzi PhD Thesis                                                 SOFTSUSY4.1.9, Standard Model", 
#          fontsize = 9, loc = "right")
#plt.title(r"C. Rizzi PhD Thesis                       tan($\beta$)="+str(args.tanb)+", $\eta$="+str(args.eta))
plt.title(r"tan($\beta$)="+str(args.tanb)+", $\eta$="+str(args.eta))

pdf_name = "../BR_higgsino_tanb"+str(args.tanb).replace(".","-")+"_eta"+str(args.eta).replace(".","-")+".pdf"
plt.savefig(pdf_name)
