
<script lang="ts">
	import { results, type PointsTableDS, type ResultsDS } from "$lib/data";
	import ResultBox from "./ResultBox.svelte";
	import Text from "./Text.svelte";


interface Props {
	team: PointsTableDS,
	position: number
}

let { team, position }: Props = $props();
const result: ResultsDS = results.find(r => r.team === team.team) || results[0];
const { simulations } = result;

</script>

<tr>
	<td>{position}</td>
	<td class="text-left font-bold text-base">
		<Text text={team.team} mobile={team.abbr} />
	</td>
	<td>{team.matches}</td>
	<td>{team.wins}</td>
	<td>{team.losses}</td>
	<td class="font-bold text-xl">{team.points}</td>
	<td>{team.nrr}</td>
</tr>

<tr class="border-b-2 border-purple-500 last:border-b-0">
	<td colspan="7" class="text-center">
		<section class="grid grid-cols-4">
			<ResultBox positive={result.top2} {simulations} header="Top 2" footer="on Points" />
			<ResultBox positive={result.top2nrr} {simulations} header="Top 2" footer="on NRR" />
			<ResultBox positive={result.top4} {simulations} header="Top 4" footer="on Points" />
			<ResultBox positive={result.top4nrr} {simulations} header="Top 4" footer="on NRR" />
		</section>
	</td>
</tr>
