import dataJson from './data.json';
import resultsJson from './results.json';



export interface PointsTableDS {
	team: string;
	abbr: string;
	matches: number;
	wins: number;
	losses: number;
	ties: number;
	no_results: number;
	points: number;
	nrr: number;
};

export interface MatchDS {
	teams: string[];
	finished: boolean;
};

export const pointsTable: PointsTableDS[] = dataJson.pointsTable;
export const matches: MatchDS[] = dataJson.matches;

export interface ResultsDS {
	team: string;
	top2: number;
	top2nrr: number;
	top4: number;
	top4nrr: number;
	simulations: number;
}

export const results: ResultsDS[] = resultsJson.results;
