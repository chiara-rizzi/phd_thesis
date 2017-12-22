from ROOT import *
import math

print "ciao Chiara"

c = TCanvas()
c.cd()


tc = 2

#fb = TF1("fb","TMath::Gaus(x,95,30,true)",0,150);
#fb = TF1("fb","Math::noncentral_chisquared_pdf(x,1,1)",0,15);
fb = TF1("fb","ROOT::Math::noncentral_chisquared_pdf(x,1,15)",0,15);
fb.SetLineColor(kRed)
#fb.SetFillColorAlpha(kRed, 0.5)
fb.GetXaxis().SetTitle("t")
fb.GetXaxis().SetTitleSize(0.06)
fb.GetXaxis().SetTitleOffset(0.4)
fb.GetYaxis().SetTitle("f(t)")
fb.GetYaxis().SetTitleSize(0.06)
fb.GetYaxis().SetTitleOffset(0.4)
fb.GetXaxis().SetLabelSize(0)
fb.GetYaxis().SetLabelSize(0)
fb.GetXaxis().SetTickLength(0)
fb.GetYaxis().SetTickLength(0)


#fs = TF1("fs","TMath::Gaus(x,60,20,true)",0,15);
fs = TF1("fs","ROOT::Math::chisquared_pdf(x,1,0)", 0, 15);
fs.SetLineColor(kBlue)
#mymax = max(fb.GetMaximum(), fb.GetMaximum())
#print mymax
fb.SetMaximum(2.5)
fb.Draw("")
fs.Draw("same")

tcut = TLine(tc, 0, tc,  1.2)
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
t.DrawLatex(tc - tc/30, -0.002, "t_{obs}")


leg = TLegend(0.7,0.6,0.89,0.8)
leg.AddEntry(fs,"f(q_{#mu}|#mu=1)","l")
leg.AddEntry(fb,"f(q_{#mu}|#mu=0)","l")
leg.AddEntry(g_pmu,"p_{#mu}","f")
leg.AddEntry(g_pb,"p_{b}","f")
leg.SetLineWidth(0)

leg.Draw()

#print fs.Integral(0,15)
#%print fb.Integral(0,15)

c.SaveAs("pmu_pb.pdf")
