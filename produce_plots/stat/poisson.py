from ROOT import *
import math

print "ciao Chiara"

c = TCanvas()
c.cd()

fb = TF1("fb","TMath::Poisson(x,50)",0,200);
fb.Draw()

fs = TF1("fs","TMath::Poisson(x,150)",0,200);
fb.Draw()
fs.SetLineColor(kBlue)
fs.Draw()

c.SaveAs("mytest.pdf")
