# coding utf-8

def components_density_profile(atoms, distribution, scale):
   fluctuations = 200 # to handle with drift to negative idicies

   for i in range(1, len(atoms)):
      distr[fluctuations + int(atoms[i][3] * scale)][0] += 1
      distr[fluctuations + int(atoms[i][3] * scale)][lat.define_phase(i + 1)] += 1

   return distr
