#! /usr/bin/env python
# Author: Izaak Neutelings (June 2020)
# Description: Test script for Plot class
#   test/plotHists.py && eog plots/testHists*.png
from TauFW.common.tools.file import ensuredir
from TauFW.Plotter.plot.Plot import Plot, CMSStyle
from ROOT import TH1D, gRandom
from TauFW.Plotter.plot.utils import LOG
LOG.verbosity = 2


def plothist(xtitle,hists,ratio=False,logy=False,norm=False):
  
  # SETTING
  outdir   = ensuredir("plots/")
  fname    = outdir+"testHists"
  if ratio:
    fname += "_ratio"
  if logy:
    fname += "_logy"
  if norm:
    fname += "_norm" # normalize each histogram
  rrange   = 0.5
  header   = "Gaussians"     # legend header
  text     = "#mu#tau_{h}"   # corner text
  grid     = True #and False
  staterr  = True and False  # add uncertainty band to first histogram
  lstyle   = 1               # solid lines
  
  # PLOT
  LOG.header(fname)
  plot = Plot(xtitle,hists,norm=norm)
  plot.draw(ratio=ratio,logy=logy,ratiorange=rrange,lstyle=lstyle,grid=grid,staterr=staterr)
  plot.drawlegend(header=header)
  plot.drawcornertext(text)
  plot.saveas(fname+".png")
  #plot.saveas(fname+".C")
  #plot.saveas(fname+".png",fname+".C")
  #plot.saveas(fname,ext=['png','pdf'])
  plot.close()
  print
  

def createhists():
  nhist    = 3
  nbins    = 50
  xmin     = 0
  xmax     = 100
  nevts    = 10000
  rrange   = 0.5
  hists    = [ ]
  gRandom.SetSeed(1777)
  for i in xrange(1,nhist+1):
    mu     = 48+i
    sigma  = 10
    hname  = "hist%d"%(i)
    htitle = "#mu = %s, #sigma = %s"%(mu,sigma)
    hist   = TH1D(hname,hname,nbins,xmin,xmax)
    for j in xrange(nevts):
      hist.Fill(gRandom.Gaus(mu,sigma))
    hists.append(hist)
  return hists
  

def main():
  
  CMSStyle.setCMSEra(2018)
  xtitle   = "p_{T}^{MET} [GeV]"
  #xtitle   = "Leading jet p_{T} [GeV]"
  
  #plothist(variable,hists,ratio=False,logy=False)
  for ratio in [True,False]:
    for logy in [True,False]:
      for norm in [True,False]:
        hists = createhists()
        plothist(xtitle,hists,ratio=ratio,logy=logy,norm=norm)
  

if __name__ == "__main__":
  main()
  