import numpy as np
import uncertainties as unc
import uncertainties.unumpy as u

#%% todo en m, kg

k_1 = 1.875
k_2 = 4.694

error_d_a = 0.00005 #0.02 mm
error_d_l = 0.00005 #0.02 mm

error_long = 0.05 #0.5 cm
error_pes = 0.00002 #0.002 g

def I_in_a(d):
    d_unc = unc.ufloat(d, error_d_a)  # Assuming an arbitrary error for d
    return (np.pi * (d_unc ** 4)) / 64

def I_in_l(d):
    d_unc = unc.ufloat(d, error_d_l)  # Assuming an arbitrary error for d
    return (np.pi * (d_unc ** 4)) / 64


def Den(long, pes):
    long_unc = unc.ufloat(long, error_long)
    pes_unc = unc.ufloat(pes, error_pes)
    return (long_unc / pes_unc)

I_acero = I_in_a(0.00606)
I_laton = I_in_l(0.00505)

error_I_acero = I_acero.std_dev
error_I_laton = I_laton.std_dev

Den_l = Den(0.50, 0.091044)
Den_a = Den(0.51, 0.119987)

error_Den_l = Den_l.std_dev
error_Den_a = Den_a.std_dev

#%% funciones laton

def dec_f_l(w, E, k):
    w_unc = unc.ufloat(w, error_w)
    E_unc = unc.ufloat(E, error_E)
    I_laton_unc = unc.ufloat(I_laton, error_I_laton)
    Den_l_unc = unc.ufloat(Den_l, error_Den_l)
    return ((w_unc**2 - (I_laton_unc * E_unc / Den_l_unc) * k )**(1/2))

def frec_f_l(E, k, dec):
    E_unc = unc.ufloat(E, error_E)
    I_laton_unc = unc.ufloat(I_laton, error_I_laton)
    Den_l_unc = unc.ufloat(Den_l, error_Den_l)
    dec_unc = unc.ufloat(dec, error_dec)
    return ((I_laton_unc * E_unc / Den_l_unc) * k**(4) + dec_unc**(2) )**(1/2)

def E_f_l(w, dec, k):
    w_unc = unc.ufloat(w, error_w)
    I_laton_unc = unc.ufloat(I_laton, error_I_laton)
    Den_l_unc = unc.ufloat(Den_l, error_Den_l)
    dec_unc = unc.ufloat(dec, error_dec)
    return ((w_unc**(2) - dec_unc**(2)) * (Den_l_unc)/ (I_laton_unc * k**(4)))



#%%funciones acero

def dec_f_a(w, E, k):
    w_unc = unc.ufloat(w, error_w)
    E_unc = unc.ufloat(E, error_E)
    I_acero_unc = unc.ufloat(I_acero, error_I_acero)
    Den_a_unc = unc.ufloat(Den_acero, error_Den_a)
    return ((w_unc**2 - (I_acero_unc * E_unc / Den_a_unc) * k )**(1/2))

def frec_f_a(E, k, dec):
    E_unc = unc.ufloat(E, error_E)
    I_acero_unc = unc.ufloat(I_acero, error_I_acero)
    Den_a_unc = unc.ufloat(Den_a, error_Den_a)
    dec_unc = unc.ufloat(dec, error_dec)
    return ((I_acero_unc * E_unc / Den_a_unc) * k**(4) + dec_unc**(2) )**(1/2)

def E_f_a(w, dec, k):
    w_unc = unc.ufloat(w, error_w)
    I_acero_unc = unc.ufloat(I_acero, error_I_acero)
    Den_a_unc = unc.ufloat(Den_a, error_Den_a)
    dec_unc = unc.ufloat(dec, error_dec)
    return ((w_unc**(2) - dec_unc**(2)) * (Den_a_unc)/ (I_acero_unc * k**(4)))




