
<script lang="ts">
	
import { pointsTable } from "$lib/data";

</script>

<svelte:head>
	<title>IPL 2025 Chances</title>
</svelte:head>

<section class="py-6">
	<table class="table max-w-3xl mx-auto text-right">
		<thead>
			<tr>
				<th class="text-left">Team</th>
				<th>Matches</th>
				<th>Won</th>
				<th>Lost</th>
				<th>Points</th>
				<th>NRR</th>
			</tr>
		</thead>

		<tbody>
			{#each pointsTable as team}
				<tr>
					<td class="text-left">{team.team}</td>
					<td>{team.matches}</td>
					<td>{team.wins}</td>
					<td>{team.losses}</td>
					<td>{team.points}</td>
					<td>{team.nrr}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</section>
