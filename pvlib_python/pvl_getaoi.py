# Autogenerated with SMOP version 0.23
# /usr/local/bin/smop pvl_getaoi.m -o python/pvl_getaoi.py
import pandas as pd
import numpy as np
import pvl_tools
def pvl_getaoi(**kwargs):
	Expect={'DataFrame':'df',
			'SurfTilt':('num','x>=0'),
			'SurfAz':('num','x>=-180','x<=180'),
			'SunZen':('matelement','num','array','x>=0'),
			'SunAz':('matelement','num','array','x>=0')
	}
	var=pvl_tools.Parse(kwargs,Expect)
	AOI=np.degrees(np.arccos(np.cos(np.radians(var.DataFrame.SunZen))*(np.cos(np.radians(var.SurfTilt))) + np.sin(np.radians(var.SurfTilt))*(np.sin(np.radians(var.DataFrame.SunZen)))*(np.cos(np.radians(var.DataFrame.SunAz) - np.radians(var.SurfAz))))) #Duffie and Beckmann 1.6.3
	
	var.DataFrame['AOI']=AOI

	return var.DataFrame