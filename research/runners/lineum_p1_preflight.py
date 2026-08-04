from dataclasses import dataclass, replace
import json, math, platform, sys, time
import numpy as np

@dataclass(frozen=True)
class C:
    dt: float=.1; psi_diffusion: float=.05; phi_diffusion: float=.05
    reaction_strength: float=.0007; drift_strength: float=0.
    mu_eta: float=.005; mu_rho: float=.0001; mu_cap: float=10.
    mu_peak_cutoff_ratio: float=.1; psi_amp_cap: float=1e6; phi_cap: float=1e6

def lap(a):
    return np.roll(a,1,0)+np.roll(a,-1,0)+np.roll(a,1,1)+np.roll(a,-1,1)-4*a

def step(s,c):
    p=np.asarray(s["psi"],complex).copy(); f=np.asarray(s["phi"],float).copy()
    m=np.asarray(s["mu"],float).copy(); k=np.asarray(s["kappa"],float)
    mul=1+m; fi=np.clip(f,0,10)
    q=.1*np.tanh((.04*fi*k*mul)/.1)*p; q/=1+np.abs(q)/10
    gy,gx=np.gradient(f); flow=c.drift_strength*(gy+1j*gx)*k*mul
    flow/=1+np.abs(flow)/10
    p+=flow*c.dt
    mag=np.abs(p); z=mag>c.psi_amp_cap
    if np.any(z): p[z]*=c.psi_amp_cap/(mag[z]+1e-30)
    p+=q*c.dt; p-=.005*p*c.dt; p+=c.psi_diffusion*lap(p)*k*c.dt
    e=np.abs(p)**2; a=c.reaction_strength*(128/p.shape[0])**2
    f+=k*a*(e-f)*c.dt; f+=k*c.phi_diffusion*.05*lap(f)*c.dt
    f=np.clip(f,0,c.phi_cap)
    floor=c.mu_peak_cutoff_ratio
    if 0<floor<1: floor*=float(np.max(e))
    m+=c.mu_eta*np.maximum(e-floor,0)*k*mul*c.dt; m-=c.mu_rho*m*c.dt
    m=np.clip(m,0,c.mu_cap)
    if not all(np.all(np.isfinite(x)) for x in (p,f,m)): raise FloatingPointError
    if np.max(np.abs(p))>=.99*c.psi_amp_cap: raise FloatingPointError
    return {"psi":p,"phi":f,"mu":m,"kappa":k.copy()}

def xy(n):
    a=np.arange(n,dtype=float)-(n-1)/2
    return np.meshgrid(a,a,indexing="xy")

def norm(a):
    return np.asarray(a,complex)/math.sqrt(float(np.sum(np.abs(a)**2)))

def pair(n=64,sep=12.,w=3.5):
    x,y=xy(n); g=lambda dx,dy: np.exp(-(dx*dx+dy*dy)/(2*w*w))
    return norm(g(x-sep/2,y)+g(x+sep/2,y)),norm(g(x,y-sep/2)+g(x,y+sep/2))

def quad(a):
    a=np.maximum(np.asarray(a,float),0); t=float(a.sum())
    if t<=0:return 0.
    x,y=xy(a.shape[0]); cx=float((a*x).sum()/t); cy=float((a*y).sum()/t)
    dx=x-cx;dy=y-cy
    return float((a*(dx*dx-dy*dy)).sum()/((a*(dx*dx+dy*dy)).sum()+1e-30))

def rms(a): return float(np.sqrt(np.mean(np.abs(a)**2)))
def rel(a,b): return float(np.linalg.norm(a-b)/(np.linalg.norm(a)+1e-30))
def shape(a,b):
    na=float(np.linalg.norm(a));nb=float(np.linalg.norm(b))
    return 0. if na==nb==0 else float(np.linalg.norm(a/na-b/nb))

def cm(a,b,ra,rb):
    qa,qb=quad(a),quad(b); xa,xb=rms(a),rms(b)
    pa="A" if qa>1e-6 else ("B" if qa<-1e-6 else "U")
    pb="A" if qb>1e-6 else ("B" if qb<-1e-6 else "U")
    return {"rms_A":xa,"rms_B":xb,"relative_signal_A":xa/(ra+1e-30),
      "relative_signal_B":xb/(rb+1e-30),"quadrupole_A":qa,"quadrupole_B":qb,
      "prediction_A":pa,"prediction_B":pb,"opposite_correct_signs":pa=="A" and pb=="B",
      "max_A":float(a.max()),"max_B":float(b.max()),
      "finite":bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b))),
      "transpose_relative_l2":rel(a,b.T)}

def main():
    t=time.perf_counter(); c=C(); pa,pb=pair(); n=64
    z=np.zeros((n,n)); k=np.ones((n,n))
    ea=float(np.sum(abs(pa)**2));eb=float(np.sum(abs(pb)**2))
    initial={"relative_energy_mismatch":abs(ea-eb)/max(ea,eb),
      "sorted_amplitude_max_mismatch":float(np.max(np.abs(np.sort(abs(pa).ravel())-np.sort(abs(pb).ravel())))),
      "quadrupole_A":quad(abs(pa)**2),"quadrupole_B":quad(abs(pb)**2)}
    initial["quadrupole_transpose_antisymmetry_error"]=abs(initial["quadrupole_A"]+initial["quadrupole_B"])
    sa={"psi":pa,"phi":z,"mu":z,"kappa":k};sb={"psi":pb,"phi":z,"mu":z,"kappa":k}
    mxp=max(np.max(abs(pa)),np.max(abs(pb)));mxf=mxm=0.
    for _ in range(120):
        sa=step(sa,c);sb=step(sb,c)
        mxp=max(mxp,float(np.max(abs(sa["psi"]))),float(np.max(abs(sb["psi"]))))
        mxf=max(mxf,float(sa["phi"].max()),float(sb["phi"].max()))
        mxm=max(mxm,float(sa["mu"].max()),float(sb["mu"].max()))
    rr={"phi_A":rms(sa["phi"]),"phi_B":rms(sb["phi"]),"mu_A":rms(sa["mu"]),"mu_B":rms(sb["mu"])}
    imprint={"A":{"max_abs_psi":mxp,"max_phi":mxf,"max_mu":mxm},
      "B":{"max_abs_psi":mxp,"max_phi":mxf,"max_mu":mxm},"rms":rr,
      "phi_transpose_relative_l2":rel(sa["phi"],sb["phi"].T),
      "mu_transpose_relative_l2":rel(sa["mu"],sb["mu"].T)}
    ma0,mb0=sa["mu"].copy(),sb["mu"].copy()
    sa["psi"][:]=0;sb["psi"][:]=0;off=replace(c,mu_eta=0)
    cps=[0,100,500,1000,2000];out={};cur=0;mxoff=0.
    for cp in cps:
        for _ in range(cp-cur):
            sa=step(sa,off);sb=step(sb,off)
            mxoff=max(mxoff,float(np.max(abs(sa["psi"]))),float(np.max(abs(sb["psi"]))))
            mxf=max(mxf,float(sa["phi"].max()),float(sb["phi"].max()))
            mxm=max(mxm,float(sa["mu"].max()),float(sb["mu"].max()))
        cur=cp;ex=(1-c.mu_rho*c.dt)**cp
        oa=rms(sa["mu"])/(rr["mu_A"]+1e-30);ob=rms(sb["mu"])/(rr["mu_B"]+1e-30)
        out[str(cp)]={"phi":cm(sa["phi"],sb["phi"],rr["phi_A"],rr["phi_B"]),
          "mu":cm(sa["mu"],sb["mu"],rr["mu_A"],rr["mu_B"]),
          "max_abs_psi":max(float(np.max(abs(sa["psi"]))),float(np.max(abs(sb["psi"])))),
          "expected_mu_decay_factor":ex,"observed_mu_decay_factor_A":oa,
          "observed_mu_decay_factor_B":ob,"relative_mu_decay_error_A":abs(oa-ex)/(ex+1e-30),
          "relative_mu_decay_error_B":abs(ob-ex)/(ex+1e-30),
          "normalized_mu_shape_difference_A":shape(sa["mu"],ma0),
          "normalized_mu_shape_difference_B":shape(sb["mu"],mb0)}
    gates={"initial_energy":initial["relative_energy_mismatch"]<=1e-14,
      "initial_sorted_amplitude":initial["sorted_amplitude_max_mismatch"]<=1e-14,
      "initial_quadrupole_antisymmetry":initial["quadrupole_transpose_antisymmetry_error"]<=1e-12,
      "finite_all_checkpoints":all(out[str(x)]["phi"]["finite"] and out[str(x)]["mu"]["finite"] for x in cps),
      "source_off_psi_zero":mxoff<=1e-15,"psi_below_cap_guard":mxp<.1*c.psi_amp_cap,
      "phi_below_cap_guard":mxf<.1*c.phi_cap,"mu_below_cap_guard":mxm<.25*c.mu_cap,
      "opposite_phi_signs_when_signal_present":all(out[str(x)]["phi"]["opposite_correct_signs"] for x in cps),
      "opposite_mu_signs_when_signal_present":all(out[str(x)]["mu"]["opposite_correct_signs"] for x in cps),
      "mu_decay_matches_analytic":all(max(out[str(x)]["relative_mu_decay_error_A"],out[str(x)]["relative_mu_decay_error_B"])<=1e-12 for x in cps),
      "mu_shape_preserved":all(max(out[str(x)]["normalized_mu_shape_difference_A"],out[str(x)]["normalized_mu_shape_difference_B"])<=1e-12 for x in cps),
      "phi_transpose_symmetry":all(out[str(x)]["phi"]["transpose_relative_l2"]<=1e-12 for x in cps),
      "mu_transpose_symmetry":all(out[str(x)]["mu"]["transpose_relative_l2"]<=1e-12 for x in cps)}
    return {"environment":{"python":sys.version,"numpy":np.__version__,"platform":platform.platform(),
      "machine":platform.machine(),"processor":platform.processor()},
      "configuration":{"grid_size":64,"separation":12.,"width":3.5,"shift":[0,0],
      "imprint_steps":120,"source_off_checkpoints":cps,"dt":c.dt,"mu_eta_imprint":c.mu_eta,
      "mu_eta_source_off":off.mu_eta,"mu_rho":c.mu_rho,"mu_cap":c.mu_cap},
      "initial_checks":initial,"imprint":imprint,"source_off":out,
      "maxima":{"max_source_off_abs_psi":mxoff,"max_phi_all_phases":mxf,"max_mu_all_phases":mxm},
      "gates":{k:bool(v) for k,v in gates.items()},"verdict":"preflight_passed" if all(gates.values()) else "preflight_invalid",
      "wall_clock_seconds":time.perf_counter()-t}

if __name__=="__main__": print(json.dumps(main(),indent=2,sort_keys=True))
