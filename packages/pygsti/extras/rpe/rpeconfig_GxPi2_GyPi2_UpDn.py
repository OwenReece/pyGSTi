from __future__ import division, print_function, absolute_import, unicode_literals
#*****************************************************************
#    pyGSTi 0.9:  Copyright 2015 Sandia Corporation              
#    This Software is released under the GPL license detailed    
#    in the file "license.txt" in the top-level pyGSTi directory 
#*****************************************************************

import numpy as _np
from . import rpeconfig as _rpeconfig

rpeconfig_GxPi2_GyPi2_UpDn_dict = {}
rpeconfig_GxPi2_GyPi2_UpDn_dict['fixed_axis_gate_label'] = 'Gx'
rpeconfig_GxPi2_GyPi2_UpDn_dict['fixed_axis_label'] = 'X'
rpeconfig_GxPi2_GyPi2_UpDn_dict['fixed_axis_target'] = [0,1,0,0]
rpeconfig_GxPi2_GyPi2_UpDn_dict['loose_axis_gate_label'] = 'Gy'
rpeconfig_GxPi2_GyPi2_UpDn_dict['loose_axis_label'] = 'Y'
rpeconfig_GxPi2_GyPi2_UpDn_dict['loose_axis_target'] = [0,0,1,0]
rpeconfig_GxPi2_GyPi2_UpDn_dict['auxiliary_axis_gate_label'] = 'Gz'
rpeconfig_GxPi2_GyPi2_UpDn_dict['auxiliary_axis_label'] = 'Z'
rpeconfig_GxPi2_GyPi2_UpDn_dict['rhoExpressions'] = ["0"]
rpeconfig_GxPi2_GyPi2_UpDn_dict['EExpressions'] = ["1"]
#rpeconfig_GxPi2_GyPi2_UpDn_dict['spamLabelDict'] = {'plus': (0,0), 'minus': (0,-1) }
rpeconfig_GxPi2_GyPi2_UpDn_dict['spamLabelDict'] = {'plus': ('rho0','E0'), 'minus': ('rho0','remainder') }
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha'] = _np.pi/2
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon'] = _np.pi/2
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta'] = 0 #This should always be 0.
rpeconfig_GxPi2_GyPi2_UpDn_dict['new_epsilon_func']  = lambda epsilon: (epsilon / (_np.pi/2)) - 1
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_hat_func'] =  lambda xhat, yhat, Nx, Ny: _np.arctan2((xhat-Nx/2.)/Nx,-(yhat-Ny/2.)/Ny)
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_hat_func'] =  lambda xhat, yhat, Nx, Ny:  _np.arctan2((xhat-Nx/2.)/Nx,-(yhat-Ny/2.)/Ny)
rpeconfig_GxPi2_GyPi2_UpDn_dict['Phi_hat_func'] =  lambda xhat, yhat, Nx, Ny:  _np.arctan2((xhat-Nx/2.)/Nx,-(yhat-Ny/2.)/Ny)
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_cos_prep_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_cos_prep_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_cos_germ_tuple'] = ('Gx',)
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_cos_germ_str'] = 'Gx'
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_cos_meas_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_cos_meas_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_sin_prep_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_sin_prep_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_sin_germ_tuple'] = ('Gx',)
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_sin_germ_str'] = 'Gx'
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_sin_meas_tuple'] = ('Gx',)
rpeconfig_GxPi2_GyPi2_UpDn_dict['alpha_sin_meas_str'] = 'Gx'
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_cos_prep_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_cos_prep_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_cos_germ_tuple'] = ('Gy',)
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_cos_germ_str'] = 'Gy'
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_cos_meas_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_cos_meas_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_sin_prep_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_sin_prep_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_sin_germ_tuple'] = ('Gy',)
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_sin_germ_str'] = 'Gy'
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_sin_meas_tuple'] = ('Gy',)
rpeconfig_GxPi2_GyPi2_UpDn_dict['epsilon_sin_meas_str'] = 'Gy'
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_cos_prep_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_cos_prep_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_cos_germ_tuple'] =  ('Gx','Gy','Gy','Gx','Gx','Gy','Gy','Gx')
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_cos_germ_str'] = 'GxGyGyGxGxGyGyGx'
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_cos_meas_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_cos_meas_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_sin_prep_tuple'] = ()
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_sin_prep_str'] = ''
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_sin_germ_tuple'] = ('Gx','Gy','Gy','Gx','Gx','Gy','Gy','Gx')
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_sin_germ_str'] = 'GxGyGyGxGxGyGyGx'
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_sin_meas_tuple'] = ('Gy',)
rpeconfig_GxPi2_GyPi2_UpDn_dict['theta_sin_meas_str'] = 'Gy'

rpeconfig_GxPi2_GyPi2_UpDn = _rpeconfig(rpeconfig_GxPi2_GyPi2_UpDn_dict)



#rpeconfig_GxPi2_GyPi2_UpDn_dict['make_rpe_gs_func'] = lambda alphaTrue, epsilonTrue, Zrot, withId=True :\    
#    if withId:
#        outputGateset = _setc.build_gateset( 
#            [2], [('Q0',)],['Gi','Gy','Gx'], 
#            [ "I(Q0)", "Y(%s,Q0)" % epsilonTrue, "X(%s,Q0)" % alphaTrue],
#            rhoExpressions=["0"], EExpressions=["1"], 
#            spamLabelDict={'plus': (0,0), 'minus': (0,-1) } )
#    else:
#        outputGateset = _setc.build_gateset( 
#            [2], [('Q0',)],['Gy','Gx'], 
#            [ "Y(%s,Q0)" % epsilonTrue, "X(%s,Q0)" % alphaTrue],
#            rhoExpressions=["0"], EExpressions=["1"], 
#            spamLabelDict={'plus': (0,0), 'minus': (0,-1) })
#
#    if Zrot != 0:
#        gatesetAux1 = _setc.build_gateset( 
#            [2], [('Q0',)],['Gi','Gz','Gx'], 
#            [ "I(Q0)", "Z(%s,Q0)" % Zrot, "X(pi/2,Q0)"],
#            rhoExpressions=["0"], EExpressions=["1"], 
#            spamLabelDict={'plus': (0,0), 'minus': (0,-1) })
#
#        outputGateset.set_gate('Gy',_objs.FullyParameterizedGate(
#                _np.dot( _np.dot(_np.linalg.inv(gatesetAux1['Gz']),
#                               outputGateset['Gy']),gatesetAux1['Gz'])) )
#    
#    
#    
#    SPAMdepol, gateDepol=None,
