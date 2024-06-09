import numpy as np
import json
from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="")


def simulate_costs(costs):
    mu_C = np.mean(costs)
    sigma_C = np.std(costs)

    # Simulation de Monte-Carlo pour les coûts
    n_simulations = 10000
    simulated_costs = np.random.normal(mu_C, sigma_C, n_simulations)

    # Distribution des Coûts de Production
    plt.figure(figsize=(6, 6))
    plt.hist(simulated_costs, bins=50, color='skyblue')
    plt.title('Distribution des Coûts de Production')
    plt.xlabel('Coûts ($)')
    plt.ylabel('Fréquence')
    plt.axvline(mu_C, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(mu_C + sigma_C, color='g', linestyle='dashed', linewidth=1)
    plt.axvline(mu_C - sigma_C, color='g', linestyle='dashed', linewidth=1)
    plt.tight_layout()
    plt.savefig('static/distribution_costs.png')
    plt.close()

def simulate_times(times):
    mu_T = np.mean(times)
    sigma_T = np.std(times)

    # Simulation de Monte-Carlo pour les délais de fabrication
    n_simulations = 10000
    simulated_times = np.random.triangular(6, mu_T, 12, n_simulations)

    # Distribution des Délais de Fabrication
    plt.figure(figsize=(6, 6))
    plt.hist(simulated_times, bins=50, color='lightgreen')
    plt.title('Distribution des Délais de Fabrication')
    plt.xlabel('Temps (jours)')
    plt.ylabel('Fréquence')
    plt.axvline(mu_T, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(mu_T + sigma_T, color='g', linestyle='dashed', linewidth=1)
    plt.axvline(mu_T - sigma_T, color='g', linestyle='dashed', linewidth=1)
    plt.tight_layout()
    plt.savefig('static/distribution_times.png')
    plt.close()

def simulate_defects(defect_rates):
    mu_Q = np.mean(defect_rates)
    sigma_Q = np.std(defect_rates)

    # Simulation de Monte-Carlo pour les taux de défauts
    n_simulations = 10000
    simulated_defects = np.random.normal(mu_Q, sigma_Q, n_simulations)

    # Distribution des Taux de Défauts
    plt.figure(figsize=(6, 6))
    plt.hist(simulated_defects, bins=50, color='salmon')
    plt.title('Distribution des Taux de Défauts')
    plt.xlabel('Taux de Défauts (%)')
    plt.ylabel('Fréquence')
    plt.axvline(mu_Q, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(mu_Q + sigma_Q, color='g', linestyle='dashed', linewidth=1)
    plt.axvline(mu_Q - sigma_Q, color='g', linestyle='dashed', linewidth=1)
    plt.tight_layout()
    plt.savefig('static/distribution_defects.png')
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    state = request.args.get('state')
    if state == 'cout_production':
        costs = [19800, 21600, 23300, 25000]
        simulate_costs(costs)
    elif state == 'delai_fabrication':
        times = [5.5, 7, 9.5, 11.5]
        simulate_times(times)
    else:
        defect_rates = [2.8, 2.6, 2.3, 2.1]
        simulate_defects(defect_rates)

    if request.method == 'POST':
        return redirect(url_for('index') + '?state=' + state + '#graph')
    return render_template('index.html', state=state)


if __name__ == '__main__':
    app.run(debug=True)
