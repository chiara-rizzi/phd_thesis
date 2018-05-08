int selections_1l(){

  //
  gStyle->SetOptStat(0);
  TCanvas *c_0lep = new TCanvas("c_1lep","c_1lep",800,600);
  TH2F* h_0lep = new TH2F("h_1lep","",3,0,3,2,0,2);
  h_0lep -> GetXaxis() -> SetBinLabel(1,"Low m_{eff}");
  h_0lep -> GetXaxis() -> SetBinLabel(2,"#splitline{Intermediate}{        m_{eff}}");
  h_0lep -> GetXaxis() -> SetBinLabel(3,"High m_{eff}");
  h_0lep -> GetYaxis() -> SetBinLabel(1,"6 #leq N_{jet} #leq 7");
  h_0lep -> GetYaxis() -> SetBinLabel(2,"N_{jet} #geq 8");
  c_0lep -> SetLeftMargin(0.20);
  c_0lep -> SetBottomMargin(0.15);
  c_0lep -> SetRightMargin(0.03);
  c_0lep -> SetTopMargin(0.03);
  h_0lep -> GetXaxis() -> SetLabelSize(0.08);
  h_0lep -> GetYaxis() -> SetLabelSize(0.08);

  h_0lep -> GetXaxis() -> SetTickSize(0);
  h_0lep -> GetYaxis() -> SetTickSize(0);

  h_0lep -> Draw();

  TLine *line1 = new TLine(0,1,2,1);
  line1->SetLineStyle(2);
  line1->SetLineWidth(2);
  line1->Draw("same");

  TLine *line3 = new TLine(1,0,1,2);
  line3->SetLineStyle(2);
  line3->SetLineWidth(2);
  line3->Draw("same");

  TLine *line4 = new TLine(2,0,2,2);
  line4->SetLineStyle(2);
  line4->SetLineWidth(2);
  line4->Draw("same");

  const double x_offset = 0.35;
  const double y_offset = 0.45;

  TLatex* ltxLL = new TLatex(x_offset,y_offset,"1L-IL");
  ltxLL -> SetTextFont(42);
  ltxLL -> Draw("same");

  TLatex* ltxIL = new TLatex(x_offset,1+y_offset,"1L-HL");
  ltxIL -> SetTextFont(42);
  ltxIL -> Draw("same");

  TLatex* ltxLI = new TLatex(1+x_offset,y_offset,"1L-II");
  ltxLI -> SetTextFont(42);
  ltxLI -> Draw("same");

  TLatex* ltxII = new TLatex(1+x_offset,1+y_offset,"1L-HI");
  ltxII -> SetTextFont(42);
  ltxII -> Draw("same");

  TLatex* ltxHH = new TLatex(2+x_offset,0.5+y_offset,"1L-HH");
  ltxHH -> SetTextFont(42);
  ltxHH -> Draw("same");

  c_0lep->Print("selections_1lep.pdf");
  return 1;
}





int selections_0l(){

  gStyle->SetOptStat(0);
  TCanvas *c_0lep = new TCanvas("c_0lep","c_0lep",800,600);
  TH2F* h_0lep = new TH2F("h_0lep","",3,0,3,3,0,3);
  h_0lep -> GetXaxis() -> SetBinLabel(1,"Low m_{eff}");
  h_0lep -> GetXaxis() -> SetBinLabel(2,"#splitline{Intermediate}{        m_{eff}}");
  h_0lep -> GetXaxis() -> SetBinLabel(3,"High m_{eff}");
  h_0lep -> GetYaxis() -> SetBinLabel(1,"4 #leq N_{jet} #leq 6");
  h_0lep -> GetYaxis() -> SetBinLabel(2,"7 #leq N_{jet} #leq 8");
  h_0lep -> GetYaxis() -> SetBinLabel(3,"N_{jet} #geq 9");
  c_0lep -> SetLeftMargin(0.20);
  c_0lep -> SetBottomMargin(0.15);
  c_0lep -> SetRightMargin(0.03);
  c_0lep -> SetTopMargin(0.03);
  h_0lep -> GetXaxis() -> SetLabelSize(0.08);
  h_0lep -> GetYaxis() -> SetLabelSize(0.08);

  h_0lep -> GetXaxis() -> SetTickSize(0);
  h_0lep -> GetYaxis() -> SetTickSize(0);


  h_0lep -> Draw();

  TLine *line1 = new TLine(0,1,3,1);
  line1->SetLineStyle(2);
  line1->SetLineWidth(2);
  line1->Draw("same");

  TLine *line2 = new TLine(0,2,2,2);
  line2->SetLineStyle(2);
  line2->SetLineWidth(2);
  line2->Draw("same");

  TLine *line3 = new TLine(1,0,1,3);
  line3->SetLineStyle(2);
  line3->SetLineWidth(2);
  line3->Draw("same");

  TLine *line4 = new TLine(2,0,2,3);
  line4->SetLineStyle(2);
  line4->SetLineWidth(2);
  line4->Draw("same");

  bool draw_diamond = false;
  bool draw_ellipse = false;
  bool draw_rectangle = true;
  if(draw_diamond){
    TLine *lineISR1 = new TLine(1,0,0,1);
    lineISR1->SetLineStyle(2);
    lineISR1->SetLineWidth(4);
    lineISR1->Draw("same");
    TLine *lineISR2 = new TLine(0,1,1,2);
    lineISR2->SetLineStyle(2);
    lineISR2->SetLineWidth(4);
    lineISR2->Draw("same");
    TLine *lineISR3 = new TLine(1.75,1,1,0);
    lineISR3->SetLineStyle(2);
    lineISR3->SetLineWidth(4);
    lineISR3->Draw("same");
    TLine *lineISR4 = new TLine(1.75,1,1,2);
    lineISR4->SetLineStyle(2);
    lineISR4->SetLineWidth(4);
    lineISR4->Draw("same");
  }
  if(draw_ellipse){
    TEllipse *el1 = new TEllipse(1,1,.7,.5);
    el1->Draw();
  }
  const double x_offset = 0.35;
  const double y_offset = 0.45;

  TLatex* ltxLL = new TLatex(x_offset-0.25,y_offset-0.25,"0L-LL");
  ltxLL -> SetTextFont(42);
  ltxLL -> Draw("same");

  TLatex* ltxIL = new TLatex(-0.25+x_offset,1+0.25+y_offset,"0L-IL");
  ltxIL -> SetTextFont(42);
  ltxIL -> Draw("same");

  TLatex* ltxHL = new TLatex(x_offset,2+y_offset,"0L-HL");
  ltxHL -> SetTextFont(42);
  ltxHL -> Draw("same");

  TLatex* ltxLI = new TLatex(1+0.25+x_offset,-0.25+y_offset,"0L-LI");
  ltxLI -> SetTextFont(42);
  ltxLI -> Draw("same");

  TLatex* ltxII = new TLatex(1+0.25+x_offset,1+0.25+y_offset,"0L-II");
  ltxII -> SetTextFont(42);
  ltxII -> Draw("same");

  TLatex* ltxHI = new TLatex(1+x_offset,2+y_offset,"0L-HI");
  ltxHI -> SetTextFont(42);
  ltxHI -> Draw("same");

  TLatex* ltxIH = new TLatex(2+x_offset,y_offset,"0L-LH");
  ltxIH -> SetTextFont(42);
  ltxIH -> Draw("same");

  TLatex* ltxHH = new TLatex(2+x_offset,1.5+y_offset,"0L-HH");
  ltxHH -> SetTextFont(42);
  ltxHH -> Draw("same");

  if(draw_diamond){
    TGraph *tgISR = new TGraph(4);
    tgISR -> SetPoint(0,1,0);
    tgISR -> SetPoint(1,0,1);
    tgISR -> SetPoint(2,1,2);
    tgISR -> SetPoint(3,1.75,1);
    tgISR -> SetFillColorAlpha(kGray,0.2);
    tgISR -> Draw("f");
  }
  if(draw_rectangle){
    TGraph *tgISR = new TGraph(5);
    const double offset = 0.02;
    tgISR -> SetPoint(0,offset,offset);
    tgISR -> SetPoint(1,offset,2.-offset);
    tgISR -> SetPoint(2,2.-offset,2.-offset);
    tgISR -> SetPoint(3,2.-offset,offset);
    tgISR -> SetPoint(4,offset,offset);
    tgISR -> SetLineColor(kRed);
    tgISR -> SetLineWidth(6);
    tgISR -> SetLineStyle(3);
    tgISR -> Draw("l");
  }
  TLatex* ltxLLISR = new TLatex(0.79,0.93,"0L-ISR");
  ltxLLISR -> SetTextFont(42);
  if(draw_rectangle){
    TEllipse *el1 = new TEllipse(1,1,.4,.22);
    el1 -> SetFillColorAlpha(kWhite,0.4);
    el1 -> SetLineColor(0);
    el1->Draw();
    ltxLLISR -> SetTextColor(kRed);
  }
  ltxLLISR -> Draw("same");

  c_0lep->Print("selections_0lep.pdf");
  return 1;
}


int selections(){
  selections_0l();
  selections_1l();
  return 1;
}
