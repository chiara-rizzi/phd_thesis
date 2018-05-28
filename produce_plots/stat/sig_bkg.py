import ROOT as r
import math

r.gStyle.SetOptStat(0)
r.gStyle.SetOptTitle(0)

fb = r.TFile.Open("/eos/atlas/user/c/crizzi/susy_multib/HFinputs_merged/SUSYHF_tag2.4.28-0-0/Bkg_2.4.28-0-0_skim_3b_with_wei.root","READ")
fs = r.TFile.Open("/eos/atlas/user/c/crizzi/susy_multib/HFinputs_merged/SUSYHF_tag2.4.28-0-0/Sig_2.4.28-0-0_with_wei.root","READ")

tb = fb.Get("ttbar_NoSys")
ts = fs.Get("Gtt_1800_1_NoSys")

if not tb:
    print "no ttbar"
if not ts:
    print "no sig"

hb = r.TH1F("hb","hb",20,2000,4000)
hs = r.TH1F("hs","hs",20,2000,4000)

sel="(bjets_n>=3 && met>200)*(weight_mc*weight_lumi)*3600"
tb.Draw("meff_incl>>hb",sel,"goff")
ts.Draw("meff_incl>>hs",sel+"*1.5","goff")

c = r.TCanvas()
#c.SetLogy()
c.cd()

hb.SetLineColor(r.kAzure)
hs.SetLineColor(r.kPink)
hb.SetLineWidth(2)
hs.SetLineWidth(2)

hb.GetXaxis().SetTitle("m_{eff} [GeV]")
hb.GetXaxis().SetTitleSize(0.06)
hb.GetXaxis().SetTitleOffset(0.4)
hb.GetYaxis().SetTitle("Events")
hb.GetYaxis().SetTitleSize(0.06)
hb.GetYaxis().SetTitleOffset(0.4)
hb.GetXaxis().SetLabelSize(0)
hb.GetYaxis().SetLabelSize(0)
hb.GetXaxis().SetTickLength(0)
hb.GetYaxis().SetTickLength(0)

hb.Draw()
hs.Draw("same")

leg = r.TLegend(0.7,0.68,0.89,0.89)
leg.AddEntry(hb,"Background","l")
leg.AddEntry(hs,"Signal","l")
leg.SetLineWidth(0)
leg.Draw()

text =  r.TLatex()
text.SetNDC()
text.SetTextAlign( 11 )
text.SetTextFont( 42 )
text.SetTextSize( 0.045 )
text.SetTextColor( 1 )

y = 0.82
write=["C. Rizzi PhD Thesis"]
for t in write:
    text.DrawLatex(0.21,y, t)
    y = y-0.06

sr1=2800
sr2=3400
text.SetNDC(0)

tsr1 = r.TLine(sr1, 0, sr1,  hb.GetMaximum()*0.8)
tsr1.SetLineStyle(3)
tsr1.Draw()
ar1 = r.TArrow(sr1+10,hb.GetMaximum()*0.7,sr1+200 -10, hb.GetMaximum()*0.7, 0.02)
ar1.Draw()

text.DrawLatex(sr1+20, hb.GetMaximum()*0.75, "SR")

ar1b = r.TArrow(sr1 + 10,hb.GetMaximum()*0.5,sr2 - 10 , hb.GetMaximum()*0.5, 0.02, "<>")
ar1b.Draw()
text.DrawLatex(sr1+20, hb.GetMaximum()*0.55, "SR1")

tsr2 = r.TLine(sr2, 0, sr2,  hb.GetMaximum()*0.6)
tsr2.SetLineStyle(3)
tsr2.Draw()
ar2 = r.TArrow(sr2 + 10 ,hb.GetMaximum()*0.5,sr2+200 -10, hb.GetMaximum()*0.5, 0.02)
ar2.Draw()
text.DrawLatex(sr2+20, hb.GetMaximum()*0.55, "SR2")

s_sr = hs.Integral(9,10000)
s_sr1 = hs.Integral(9,14)
s_sr2 = hs.Integral(15,1000)

b_sr = hb.Integral(9,10000)
b_sr1 = hb.Integral(9,14)
b_sr2 = hb.Integral(15,1000)

print "Signal rates"
print "SR:", s_sr
print "SR1:", s_sr1
print "SR2:", s_sr2

print ""

print "Background rates"
print "SR:", b_sr
print "SR1:", b_sr1
print "SR2:", b_sr2

print ""

print "Significances"
print "SR:", s_sr/math.sqrt(b_sr)
print "SR1:", s_sr1/math.sqrt(b_sr1)
print "SR2:", s_sr2/math.sqrt(b_sr2)


c.Update()
c.SaveAs("sig_bkg.pdf")
