#!/usr/bin/env python3

import warnings
warnings.filterwarnings('ignore')

from matplotlib import cm
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.colors import LogNorm
import matplotlib.patches as patches

from scipy.stats import gaussian_kde, norm, skewnorm
from scipy.ndimage import gaussian_filter
# from scipy.optimize import curve_fit
import pandas as pd
import _pickle as pickle
import numpy as np
import os, glob, sys, time

import astropy.io.fits as fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u

import pprint
pp = pprint.PrettyPrinter(indent=4)

plt.style.use('ggplot')

plt.rcParams['xtick.labelsize']=12
plt.rcParams['ytick.labelsize']=12
plt.rcParams['xtick.direction']='out'
plt.rcParams['ytick.direction']='out'

plt.rcParams['xtick.major.size']=10
plt.rcParams['ytick.major.size']=10
plt.rcParams['xtick.major.pad']=5
plt.rcParams['ytick.major.pad']=5

plt.rcParams['xtick.minor.size']=5
plt.rcParams['ytick.minor.size']=5
plt.rcParams['xtick.minor.pad']=5
plt.rcParams['ytick.minor.pad']=5

font_small = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

font_medium = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 20,
        }

font_large = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 24,
        }
params = {'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large',
         }
# Updates plots to apply the above formatting to all plots in doc
pylab.rcParams.update(params)