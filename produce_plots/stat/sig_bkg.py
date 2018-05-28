import ROOT as r
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sr1', default=3000, type=float)
parser.add_argument('--sr2', default=3500, type=float)
parser.add_argument('--unc', default=0.3, type=float)
parser.add_argument('--scale', default=0.76, type=float)

args = parser.parse_args()
sr1=args.sr1
sr2=args.sr2
rel_unc=args.unc

r.gStyle.SetOptStat(0)
r.gStyle.SetOptTitle(0)
r.gROOT.SetBatch()

fb = r.TFile.Open("/eos/atlas/user/c/crizzi/susy_multib/HFinputs_merged/SUSYHF_tag2.4.28-0-0/Bkg_2.4.28-0-0_skim_3b_with_wei.root","READ")
fs = r.TFile.Open("/eos/atlas/user/c/crizzi/susy_multib/HFinputs_merged/SUSYHF_tag2.4.28-0-0/Sig_2.4.28-0-0_with_wei.root","READ")

tb = fb.Get("ttbar_NoSys")
ts = fs.Get("Gtt_1800_1_NoSys")

if not tb:
    print "no ttbar"
if not ts:
    print "no sig"

nbins = 20
xmin = 2100
xmax = 4100

hb = r.TH1F("hb","hb",nbins,xmin,xmax)
hs = r.TH1F("hs","hs",nbins,xmin,xmax)

sel="(bjets_n>=3 && met>200)*(weight_mc*weight_lumi)*3600"
tb.Draw("meff_incl>>hb",sel+"*8","goff")
ts.Draw("meff_incl>>hs",sel+"*8*"+str(args.scale),"goff")

c = r.TCanvas()
#c.SetLogy()
c.cd()

hb.SetLineColor(r.kAzure)
hs.SetLineColor(r.kPink)
hb.SetLineWidth(2)
hs.SetLineWidth(2)

hb.GetXaxis().SetTitle("m_{eff}")
#hb.GetXaxis().SetTitleSize(0.06)
#hb.GetXaxis().SetTitleOffset(0.4)
hb.GetYaxis().SetTitle("Events")
#hb.GetYaxis().SetTitleSize(0.06)
#hb.GetYaxis().SetTitleOffset(0.4)
#hb.GetXaxis().SetLabelSize(0)
#hb.GetYaxis().SetLabelSize(0)
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

bin1 = int((sr1 - xmin)/((xmax-xmin)/nbins))+1
bin2 = int((sr2 - xmin)/((xmax-xmin)/nbins))+1
print "bin1",bin1
print "bin2",bin2

s_sr = hs.Integral(bin1,10000)
s_sr1 = hs.Integral(bin1, bin2-1)
s_sr2 = hs.Integral(bin2,1000)

b_sr = hb.Integral(bin1,10000)
b_sr1 = hb.Integral(bin1, bin2-1)
b_sr2 = hb.Integral(bin2, 1000)

print "Signal rates"
print "SR:", s_sr
print "SR1:", s_sr1
print "SR2:", s_sr2
print "sum", s_sr1+s_sr2

print ""

print "Background rates"
print "SR:", b_sr
print "SR1:", b_sr1
print "SR2:", b_sr2
print "sum", b_sr1+b_sr2

"""
print ""
print "S/sqrt(B)"
print "SR:", s_sr/math.sqrt(b_sr)
print "SR1:", s_sr1/math.sqrt(b_sr1)
print "SR2:", s_sr2/math.sqrt(b_sr2)
"""
print ""
r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr, b_sr, rel_unc)
print "significance"
print "SR:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr, b_sr, rel_unc)
print "SR1:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr1, b_sr1, rel_unc)
print "SR2:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr2, b_sr2, rel_unc)
print "qaud:", math.sqrt(r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr1, b_sr1, rel_unc)*r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr1, b_sr1, rel_unc) + r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr2, b_sr2, rel_unc)*r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr2, b_sr2, rel_unc)    )

print ""

print "**************"
print "SR:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr, b_sr, rel_unc)
print "**************"

c.Update()
c.SaveAs("sig_bkg.pdf")
