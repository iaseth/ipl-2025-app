
<script lang="ts">
	
import RainbowBorder from "$lib/components/RainbowBorder.svelte";
import TeamRow from "$lib/components/TeamRow.svelte";
import Text from "$lib/components/Text.svelte";
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
				<th>
					<Text text="Matches" mobile="M" />
				</th>
				<th>
					<Text text="Won" mobile="W" />
				</th>
				<th>
					<Text text="Lost" mobile="L" />
				</th>
				<th>
					<Text text="Points" mobile="P" />
				</th>
				<th>NRR</th>
			</tr>
		</thead>

		<tbody>
			{#each pointsTable as team, index}
				<TeamRow {team} position={index+1} />
			{/each}
		</tbody>
	</table>
</section>

<footer class="h-20"></footer>

<footer class="footer sm:footer-horizontal footer-center bg-base-300 text-base-content px-4 py-12">
	<aside>
		<p>Copyright © {new Date().getFullYear()} Ankur Seth</p>
	</aside>
</footer>

<RainbowBorder />
