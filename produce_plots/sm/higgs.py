from ROOT import *
import math

print "ciao Chiara"

gStyle.SetOptTitle(0)

def plot(fb, name):
    
    c = TCanvas("can","can",600,900)
    c.cd()
#fb = TF2("fb","-2000*x*y + 3*(x*x*y*y)",-10,10,-10,10);
#fb.SetLineColor(kRed)
#fb.SetFillColorAlpha(kRed, 0.5)
    fb.GetZaxis().SetTitle("V(#phi)")
    fb.GetZaxis().SetTitleSize(0.06)
    fb.GetZaxis().SetTitleOffset(0.4)
    fb.GetXaxis().SetTitle("Re(#phi)")
    fb.GetXaxis().SetTitleSize(0.06)
    fb.GetXaxis().SetTitleOffset(0.4)
    fb.GetYaxis().SetTitle("Im(#phi)")
    fb.GetYaxis().SetTitleSize(0.06)
    fb.GetYaxis().SetTitleOffset(0.4)
    fb.GetXaxis().SetLabelSize(0)
    fb.GetYaxis().SetLabelSize(0)
    fb.GetZaxis().SetLabelSize(0)
    fb.GetXaxis().SetTickLength(0)
    fb.GetYaxis().SetTickLength(0)
    fb.GetZaxis().SetTickLength(0)
    fb.Draw("SURF2")
    #t = TLatex()
    #t.DrawLatex(tc - tc/30, -0.002, "t_{obs}")
    c.SaveAs(name+".pdf")

fb = TF2("fb","(1-(x**2+y**2))**2",-1,1,-1,1);
plot(fb, "higgs_negmu2")
fb2 = TF2("fb2","(1+(x**2+y**2))**2",-1,1,-1,1);
plot(fb2, "higgs_posmu2")
