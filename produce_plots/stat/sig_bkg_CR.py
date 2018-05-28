import ROOT as r
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cr', default=2000, type=float)
parser.add_argument('--sr', default=3000, type=float)
parser.add_argument('--unc', default=0.3, type=float)
parser.add_argument('--scale', default=0.76, type=float)

args = parser.parse_args()
cr=args.cr
sr=args.sr
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

nbins = 36
xmin = 500
xmax = 4100

hb = r.TH1F("hb","hb",nbins,xmin,xmax)
hs = r.TH1F("hs","hs",nbins,xmin,xmax)

sel="(bjets_n>=3 && met>200)*(weight_mc*weight_lumi)*3600"
tb.Draw("meff_incl>>hb",sel+"*8","goff")
ts.Draw("meff_incl>>hs",sel+"*8*"+str(args.scale),"goff")

c = r.TCanvas()
c.SetLogy()
c.cd()

hb.SetMaximum(50*hb.GetMaximum())

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

tcr = r.TLine(cr, 0, cr,  hb.GetMaximum()*0.05)
tcr.SetLineStyle(3)
tcr.Draw()
ar1 = r.TArrow(cr-10,hb.GetMaximum()*0.01,cr-500 +10, hb.GetMaximum()*0.01, 0.02)
ar1.Draw()
text.DrawLatex(cr-700, hb.GetMaximum()*0.02, "CR")

tsr = r.TLine(sr, 0, sr,  hs.GetMaximum()*9)
tsr.SetLineStyle(3)
tsr.Draw()
ar2 = r.TArrow(sr +10,hs.GetMaximum()*5,sr+500 -10, hs.GetMaximum()*5, 0.02)
ar2.Draw()
text.DrawLatex(sr+50, hs.GetMaximum()*6, "SR")


bin1 = int((cr - xmin)/((xmax-xmin)/nbins))+1
print "bin1",bin1
bin2 = int((sr - xmin)/((xmax-xmin)/nbins))+1
print "bin2",bin2


s_cr = hs.Integral(-1,bin1)
b_cr = hb.Integral(-1,bin1)
s_sr = hs.Integral(bin2,10000)
b_sr = hb.Integral(bin2,10000)

print "Rates CR"
print "Sig:", s_cr
print "Bkg", b_cr
print "S/B:", s_cr/b_cr
print ""
print "Rates SR"
print "Sig:", s_sr
print "Bkg", b_sr
print "S/B:", s_sr/b_sr


c.Update()
c.SaveAs("sig_bkg_CR.pdf")
