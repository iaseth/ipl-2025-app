import argparse
import json

from tabulate import tabulate
import numpy as np
import pandas as pd



DATA_JSON_PATH = "src/lib/data.json"
SIMULATIONS_JSON_PATH = "src/lib/results.json"

TEAMS_ABBRS = {
	'Gujarat Titans': "GT",
	'Delhi Capitals': "DC",
	'Royal Challengers Bengaluru': "RCB",
	'Mumbai Indians': "MI",
	'Punjab Kings': "PBKS",
	'Lucknow Super Giants': "LSG",
	'Kolkata Knight Riders': "KKR",
	'Rajasthan Royals': "RR",
	'Sunrisers Hyderabad': "SRH",
	'Chennai Super Kings': "CSK"
}


def get_saved_data():
	with open(DATA_JSON_PATH) as f:
		jo = json.load(f)
	return jo


def simulate_top_finishes(points, matches, n_simulations=10000, seed=None):
	import numpy as np
	import pandas as pd

	if seed is not None:
		np.random.seed(seed)

	n_teams = len(points)

	# Initialize counters
	top2_strict = np.zeros(n_teams, dtype=int)
	top2_tied = np.zeros(n_teams, dtype=int)
	top4_strict = np.zeros(n_teams, dtype=int)
	top4_tied = np.zeros(n_teams, dtype=int)

	for _ in range(n_simulations):
		sim_points = np.array(points, copy=True)
		for team1, team2 in matches:
			winner = np.random.choice([team1, team2])
			sim_points[winner] += 2

		sorted_teams = np.argsort(-sim_points)
		sorted_points = sim_points[sorted_teams]

		# Cutoff points for top 2 and top 4
		top2_cutoff = sorted_points[1]
		top4_cutoff = sorted_points[3]

		# Teams tied at or above cutoff
		tied_top2_teams = np.where(sim_points >= top2_cutoff)[0]
		tied_top4_teams = np.where(sim_points >= top4_cutoff)[0]

		# Strict top 2
		if sorted_points[1] != sorted_points[2]:
			for i in range(2):
				top2_strict[sorted_teams[i]] += 1
		else:
			for team in tied_top2_teams:
				top2_tied[team] += 1

		# Strict top 4
		if sorted_points[3] != sorted_points[4]:
			for i in range(4):
				top4_strict[sorted_teams[i]] += 1
		else:
			for team in tied_top4_teams:
				top4_tied[team] += 1

	# Convert to percentages
	def get_results(i):
		results = [ top2_strict[i], top2_tied[i], top4_strict[i], top4_tied[i] ]
		results = [int(x) for x in results]
		return results

	return [get_results(i) for i, p in enumerate(points)]


def print_matches(jo):
	rows = [[
		i+1, m['teams'][0], m['teams'][1],
		"Completed" if m['finished'] else "TBC"
	] for i, m in enumerate(jo['matches'])]
	print(tabulate(rows, headers=["#", "Team 1", "Team 2", "Status"]))


def print_points_table(jo):
	print(tabulate(jo['pointsTable']))


def get_probabilities(jo, n_simulations):
	teams = list(TEAMS_ABBRS.keys())
	teams.sort()

	team_indices = { team: i for i, team in enumerate(teams) }

	matches = [m['teams'] for m in jo['matches'] if not m['finished']]
	matches = [[ team_indices[m[0]], team_indices[m[1]] ] for m in matches]

	points = [[ team_indices[team['team']], team['points'] ] for team in jo['pointsTable']]
	points.sort(key=lambda x:x[0])
	points = list(map(lambda x:x[1], points))

	probabilities = simulate_top_finishes(points, matches, n_simulations=n_simulations)
	return (teams, points, probabilities)


def print_probabilities(jo, n_simulations):
	teams, points, probabilities = get_probabilities(jo, n_simulations)
	for i, team in enumerate(teams):
		pb = probabilities[i]
		print(f"{team:30} {points[i]:4}", end="")
		for p in pb:
			pp = 100 * p / n_simulations
			print(f"{pp:10.2f}", end="")
		print()


def save_probabilities(jo, n_simulations):
	teams, points, probabilities = get_probabilities(jo, n_simulations)
	results = [{
		'team': team,
		'top2': probabilities[i][0],
		'top2nrr': probabilities[i][1],
		'top4': probabilities[i][2],
		'top4nrr': probabilities[i][3],
		'simulations': n_simulations,
	} for i, team in enumerate(teams)]

	jo = {}
	jo['results'] = results

	with open(SIMULATIONS_JSON_PATH, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"Saved: {SIMULATIONS_JSON_PATH}")


def main():
	parser = argparse.ArgumentParser(description="Simulate IPL 2025.")
	parser.add_argument("command", help="Name of the command")
	parser.add_argument("-n", type=int, default=1000, help="Number of simulations")

	args = parser.parse_args()
	jo = get_saved_data()
	command = args.command.upper()

	match command:
		case 'MATCHES': print_matches(jo)
		case 'TABLE': print_points_table(jo)
		case 'SIM': print_probabilities(jo, n_simulations=args.n)
		case 'SAVE': save_probabilities(jo, n_simulations=args.n)
		case _:
			print(f"Unknow command: '{args.command}'")


if __name__ == '__main__':
	main()
