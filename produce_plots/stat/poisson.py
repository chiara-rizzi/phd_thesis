from ROOT import *
import math

print "ciao Chiara"

c = TCanvas()
c.cd()

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)


tc = 3

#fb = TF1("fb","TMath::Gaus(x,95,30,true)",0,150); #fb = TF1("fb","Math::noncentral_chisquared_pdf(x,1,1)",0,15);
fb = TF1("fb","ROOT::Math::noncentral_chisquared_pdf(x,4,2)",1,8);
fb.SetLineColor(kRed)
#fb.SetFillColorAlpha(kRed, 0.5)

#fs = TF1("fs","TMath::Gaus(x,60,20,true)",0,15);
fs = TF1("fs","ROOT::Math::chisquared_pdf(x,1,0)", 1, 8);
fs.SetLineColor(kBlue)

fs.GetXaxis().SetTitle("t")
fs.GetXaxis().SetTitleSize(0.06)
fs.GetXaxis().SetTitleOffset(0.4)
fs.GetYaxis().SetTitle("f(t)")
fs.GetYaxis().SetTitleSize(0.06)
fs.GetYaxis().SetTitleOffset(0.4)
fs.GetXaxis().SetLabelSize(0)
fs.GetYaxis().SetLabelSize(0)
fs.GetXaxis().SetTickLength(0)
fs.GetYaxis().SetTickLength(0)


#mymax = max(fb.GetMaximum(), fb.GetMaximum())
#print mymax
#fb.SetMaximum(2.5)
fs.Draw("")
fb.Draw("same")

tcut = TLine(tc, 0, tc,  fs.GetMaximum())
tcut.SetLineStyle(3)
tcut.Draw()

g_pmu = TGraph()
g_pmu.SetPoint(0,tc,0)
for i in [tc+step*0.1 for step in range(0, (15-tc)*10)]:
    #print i
    g_pmu.SetPoint(g_pmu.GetN(), i, fs.Eval(i))
g_pmu.SetFillColorAlpha(kBlue,0.5)
g_pmu.Draw("f same")

g_pb = TGraph()
g_pb.SetPoint(g_pb.GetN(), 0, 0)
for i in [step*0.01 for step in range(0, (tc)*100)]:
    #print i
    g_pb.SetPoint(g_pb.GetN(), i, fb.Eval(i))
g_pb.SetPoint(g_pb.GetN(), tc, 0)
g_pb.SetFillColorAlpha(kRed,0.5)
g_pb.Draw("f same")


t = TLatex()
t.DrawLatex(tc - tc/30, -0.02, "t_{obs}")


leg = TLegend(0.7,0.65,0.89,0.85)
leg.AddEntry(fs,"f(q_{#mu}|#mu=1)","l")
leg.AddEntry(fb,"f(q_{#mu}|#mu=0)","l")
leg.AddEntry(g_pmu,"p_{#mu}","f")
leg.AddEntry(g_pb,"p_{b}","f")
leg.SetLineWidth(0)

leg.Draw()

text =  TLatex()
text.SetNDC()
text.SetTextAlign( 11 )
text.SetTextFont( 42 )
text.SetTextSize( 0.045 )
text.SetTextColor( 1 )
y = 0.82
write=["C. Rizzi PhD Thesis"]
for t in write:
    text.DrawLatex(0.37,y, t)
    y = y-0.06


#print fs.Integral(0,15)
#%print fb.Integral(0,15)

c.SaveAs("pmu_pb.pdf")
