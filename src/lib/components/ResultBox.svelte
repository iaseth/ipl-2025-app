
<script lang="ts">

interface Props {
	positive: number,
	simulations: number,
	header: string,
	footer: string
}

let { positive, simulations, header, footer }: Props = $props();
const pc = positive * 100 / simulations;

</script>

<div class="py-1 space-y-2 text-sm">
	<p class="font-bold opacity-60">{header}</p>
	<h2 class="text-xl md:text-2xl lg:text-3xl font-bold opacity-75">
		<span>{pc < 10 ? pc.toFixed(2) : pc.toFixed(1)}</span>
		<span class="text-xl">%</span>
	</h2>
	<p class="opacity-60">{footer}</p>
</div>
