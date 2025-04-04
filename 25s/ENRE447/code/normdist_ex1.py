from scipy import stats
import numpy as np
import pprint as pp

print("Normal Distribution Example")
prob_norm = stats.norm.cdf(x=62, loc=50, scale=10) - stats.norm.cdf(x=48, loc=50, scale=10)
pp.pprint(prob_norm)

print("LogNormal Distribution Example")
mu, sigma = 1, 1
prob_lognorm = stats.lognorm.cdf(x=3.5, s=sigma, scale=np.exp(mu)) - stats.lognorm.cdf(x=0.5, s=sigma, scale=np.exp(mu))
pp.pprint(prob_lognorm)
