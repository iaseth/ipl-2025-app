import dataJson from './data.json';



export interface PointsTableDS {
	team: string;
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
