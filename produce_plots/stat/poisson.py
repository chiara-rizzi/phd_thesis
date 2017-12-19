from ROOT import *
import math

print "ciao Chiara"

c = TCanvas()
c.cd()

gStyle.SetOptTitle(0)

tc = 65

fb = TF1("fb","TMath::Poisson(x,50)",25,125);
fb.SetLineColor(kRed)
#fb.SetFillColorAlpha(kRed, 0.5)
fb.SetFillColor(6)
fb.GetXaxis().SetTitle("t")
fb.GetYaxis().SetTitle("f(t)")
fb.GetXaxis().SetLabelSize(0)
fb.GetYaxis().SetLabelSize(0)
fb.GetXaxis().SetTickLength(0)
fb.GetYaxis().SetTickLength(0)
fb.Draw("F")

fs = TF1("fs","TMath::Poisson(x,75)",25,125);
fb.Draw()
fs.SetLineColor(kBlue)
fs.SetFillColorAlpha(kBlue, 0.5)
fs.Draw("fc same")

tcut = TLine(tc, 0, tc, fb.GetMaximum())
tcut.SetLineStyle(3)
tcut.Draw()

t = TLatex()
t.DrawLatex(tc - tc/30, -0.004, "t_{cut}")

print fs.Integral(0,100)
print fb.Integral(0,100)

c.SaveAs("mytest.pdf")
