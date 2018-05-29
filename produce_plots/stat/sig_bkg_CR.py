import ROOT as r
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cr', default=2200, type=float)
parser.add_argument('--sr', default=3000, type=float)
parser.add_argument('--sr2', default=3500, type=float)
parser.add_argument('--unc', default=0.3, type=float)
parser.add_argument('--scale', default=0.76, type=float)
cr_low=1600
bin0=12

args = parser.parse_args()
cr=args.cr
sr=args.sr
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

nbins = 36
xmin = 500
xmax = 4100

hb = r.TH1F("hb","hb",nbins,xmin,xmax)
hs = r.TH1F("hs","hs",nbins,xmin,xmax)

sel="(bjets_n>=3 && met>200)*(weight_mc*weight_lumi)*3600"
tb.Draw("meff_incl>>hb",sel+"*8","goff")
ts.Draw("meff_incl>>hs",sel+"*8*"+str(args.scale),"goff")

hb.SetMaximum(50*hb.GetMaximum())

hb.SetLineColor(r.kAzure)
hs.SetLineColor(r.kPink)
hb.SetLineWidth(2)
hs.SetLineWidth(2)

hb.GetXaxis().SetTitle("m_{eff} [GeV]")
#hb.GetXaxis().SetTitleSize(0.06)
#hb.GetXaxis().SetTitleOffset(0.4)
hb.GetYaxis().SetTitle("Events")
#hb.GetYaxis().SetTitleSize(0.06)
#hb.GetYaxis().SetTitleOffset(0.4)
#hb.GetXaxis().SetLabelSize(0)
#hb.GetYaxis().SetLabelSize(0)
hb.GetXaxis().SetTickLength(0)
hb.GetYaxis().SetTickLength(0)

trand = r.TRandom3(5787)
hd = hb.Clone("Data")
for i in range(0, hd.GetNbinsX()+2):
    mean = 0.87* hb.GetBinContent(i) + 0.3*hs.GetBinContent(i)     
    d_entry = trand.Poisson( mean)
    print mean, d_entry
    hd.SetBinContent(i, d_entry)
hd.SetLineColor(r.kBlack)

c = r.TCanvas()
c.SetLogy()
c.cd()

hb.Draw()
hs.Draw("same")
hd.SetMarkerStyle(20)
#hd.Draw('same')
#hb.Draw("same")

leg = r.TLegend(0.7,0.68,0.89,0.89)
leg.AddEntry(hb,"Background","l")
leg.AddEntry(hs,"Signal","l")
#leg.AddEntry(hd,"Pseudo-data","l")
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
tcr2 = r.TLine(cr_low, 0, cr_low,  hb.GetMaximum()*0.05)
tcr2.SetLineStyle(3)
tcr2.Draw()
ar1 = r.TArrow(cr-10,hb.GetMaximum()*0.01,cr_low +10, hb.GetMaximum()*0.01, 0.02, '<>')
ar1.Draw()
text.DrawLatex(cr-400, hb.GetMaximum()*0.02, "CR")

tsr = r.TLine(sr, 0, sr,  hs.GetMaximum()*100)
tsr.SetLineStyle(3)
tsr.Draw()
ar2 = r.TArrow(sr +10,hs.GetMaximum()*5,sr+500 -10, hs.GetMaximum()*5, 0.02)
ar2.Draw()
text.DrawLatex(sr+50, hs.GetMaximum()*6, "SR")

ar3 = r.TArrow(cr+10,hb.GetMaximum()*0.002,sr-10, hb.GetMaximum()*0.002, 0.02, '<>')
ar3.Draw()
text.DrawLatex(cr+300, hs.GetMaximum()*50, "VR")

print "bin0",bin0
print "starting at:", hb.GetBinLowEdge(bin0)
bin1 = int((cr - xmin)/((xmax-xmin)/nbins))+1
print "bin1",bin1
print "starting at:", hb.GetBinLowEdge(bin1)
bin2 = int((sr - xmin)/((xmax-xmin)/nbins))+1
print "bin2",bin2
print "starting at:", hb.GetBinLowEdge(bin2)
bin3 = int((sr2 - xmin)/((xmax-xmin)/nbins))+1
print "bin3",bin3
print "starting at:", hb.GetBinLowEdge(bin3)

s_cr = hs.Integral(bin0,bin1-1)
b_cr = hb.Integral(bin0,bin1-1)
d_cr = hd.Integral(bin0,bin1-1)

s_vr = hs.Integral(bin1,bin2-1)
b_vr = hb.Integral(bin1,bin2-1)
d_vr = hd.Integral(bin1,bin2-1)

s_sr = hs.Integral(bin2,10000)
b_sr = hb.Integral(bin2,10000)
d_sr = hd.Integral(bin2,10000)

s_sr1 = hs.Integral(bin2, bin3-1)
b_sr1 = hb.Integral(bin2, bin3-1)
d_sr1 = hd.Integral(bin2, bin3-1)

s_sr2 = hs.Integral(bin3,10000)
b_sr2 = hb.Integral(bin3,10000)
d_sr2 = hd.Integral(bin3,10000)


r.RooStats.NumberCountingUtils.BinomialExpZ( s_cr, b_cr, 0.3)

print "Rates CR"
print "Bkg", b_cr
print "Sig:", s_cr
print "S/B:", s_cr/b_cr
print "signif:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_cr, b_cr, 0.3)
print "Data", d_cr
print ""
print "Rates VR"
print "Bkg", b_vr
print "Sig:", s_vr
print "S/B:", s_vr/b_vr
print "signif:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_vr, b_vr, 0.3)
print "Data", d_vr
print ""
print "Rates SR"
print "Bkg", b_sr
print "Sig:", s_sr
print "S/B:", s_sr/b_sr
print "signif:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr, b_sr, 0.3)
print "Data", d_sr
print ""
print "Rates SR1"
print "Bkg", b_sr1
print "Sig:", s_sr1
print "S/B:", s_sr1/b_sr1
print "signif:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr1, b_sr1, 0.3)
print "Data", d_sr1
print ""
print "Rates SR2"
print "Bkg", b_sr2
print "Sig:", s_sr2
print "S/B:", s_sr2/b_sr2
print "signif:", r.RooStats.NumberCountingUtils.BinomialExpZ( s_sr2, b_sr2, 0.3)
print "Data", d_sr2

c.Update()
c.SaveAs("sig_bkg_CR.pdf")

