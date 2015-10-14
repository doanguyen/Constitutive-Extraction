#-*- coding: utf-8 -*-

import numpy as np
import sys, os, re

def cst2fdtd():
	s11linear = np.loadtxt('data/s11linear.txt',unpack=True,skiprows=2)
	s21linear = np.loadtxt('data/s21linear.txt',unpack=True,skiprows=2)
	s11arg = np.loadtxt('data/s11arg.txt',unpack=True,skiprows=2)
	s21arg = np.loadtxt('data/s21arg.txt',unpack=True,skiprows=2)
	freq,s11amp,s21amp,s11phase,s21phase = s11linear[0,:]*10**9,s11linear[1,:],s21linear[1,:],s11arg[1,:],s21arg[1,:]
	#np.savetxt('out.dat',(freq,s11amp,s21amp,s11phase,s21phase),newline="\n")
	output = np.column_stack((freq.flatten(),s11amp.flatten(),s11phase.flatten(),s21amp.flatten(),s21phase.flatten()))
	np.savetxt('output.dat',output)



cst2fdtd()
