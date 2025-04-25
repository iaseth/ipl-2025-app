
<script lang="ts">

interface Props {
	text: string,
	mobile: string
}
let { text, mobile }: Props = $props();

</script>

<span class="md:hidden">{mobile}</span>
<span class="hidden md:block">{text}</span>
