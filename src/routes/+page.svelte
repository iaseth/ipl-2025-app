
<script lang="ts">
	
import RainbowBorder from "$lib/components/RainbowBorder.svelte";
import { pointsTable } from "$lib/data";

</script>

<svelte:head>
	<title>IPL 2025 Chances</title>
</svelte:head>

<RainbowBorder />

<a class="block px-4 py-10 text-center" href="/">
	<h1 class="text-4xl font-bold mb-1">Chances</h1>
	<p class="text-sm">Created by Ankur Seth</p>
</a>

<section>
	<table class="table max-w-3xl mx-auto text-right">
		<thead>
			<tr>
				<th>#</th>
				<th class="text-left">Team</th>
				<th>Matches</th>
				<th>Won</th>
				<th>Lost</th>
				<th>Points</th>
				<th>NRR</th>
			</tr>
		</thead>

		<tbody>
			{#each pointsTable as team, index}
				<tr>
					<td>{index+1}</td>
					<td class="text-left">{team.team}</td>
					<td>{team.matches}</td>
					<td>{team.wins}</td>
					<td>{team.losses}</td>
					<td>{team.points}</td>
					<td>{team.nrr}</td>
				</tr>

				<tr hidden>
					<td></td>
					<td colspan="6" class="text-center"></td>
				</tr>
			{/each}
		</tbody>
	</table>
</section>

<footer class="h-32"></footer>

<footer class="footer sm:footer-horizontal footer-center bg-base-300 text-base-content px-4 py-12">
	<aside>
		<p>Copyright © {new Date().getFullYear()} Ankur Seth</p>
	</aside>
</footer>

<RainbowBorder />
