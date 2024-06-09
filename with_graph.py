import numpy as np
import matplotlib.pyplot as plt

# Données historiques
costs = [19800, 21600, 23300, 25000]
times = [6, 7.5, 10, 12]
defect_rates = [3.0, 2.8, 2.5, 2.3]

# Calcul des statistiques
mu_C = np.mean(costs)
sigma_C = np.std(costs)
mu_T = np.mean(times)
sigma_T = np.std(times)
mu_Q = np.mean(defect_rates)
sigma_Q = np.std(defect_rates)

# Simulation de Monte-Carlo
n_simulations = 10000
simulated_costs = np.random.normal(mu_C, sigma_C, n_simulations)
simulated_times = np.random.triangular(6, mu_T, 12, n_simulations)
simulated_defects = np.random.normal(mu_Q, sigma_Q, n_simulations)

# Affichage des résultats
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.hist(simulated_costs, bins=50, color='skyblue')
plt.title('Distribution des Coûts de Production')
plt.xlabel('Coûts ($)')
plt.ylabel('Fréquence')
plt.axvline(mu_C, color='r', linestyle='dashed', linewidth=1)
plt.axvline(mu_C + sigma_C, color='g', linestyle='dashed', linewidth=1)
plt.axvline(mu_C - sigma_C, color='g', linestyle='dashed', linewidth=1)

plt.subplot(1, 3, 2)
plt.hist(simulated_times, bins=50, color='lightgreen')
plt.title('Distribution des Délais de Fabrication')
plt.xlabel('Temps (jours)')
plt.ylabel('Fréquence')
plt.axvline(mu_T, color='r', linestyle='dashed', linewidth=1)
plt.axvline(mu_T + sigma_T, color='g', linestyle='dashed', linewidth=1)
plt.axvline(mu_T - sigma_T, color='g', linestyle='dashed', linewidth=1)

plt.subplot(1, 3, 3)
plt.hist(simulated_defects, bins=50, color='salmon')
plt.title('Distribution des Taux de Défauts')
plt.xlabel('Taux de Défauts (%)')
plt.ylabel('Fréquence')
plt.axvline(mu_Q, color='r', linestyle='dashed', linewidth=1)
plt.axvline(mu_Q + sigma_Q, color='g', linestyle='dashed', linewidth=1)
plt.axvline(mu_Q - sigma_Q, color='g', linestyle='dashed', linewidth=1)

plt.tight_layout()
plt.show()
