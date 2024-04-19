<script lang="ts">
	import type { PageData } from "./$types";

    export let data: PageData;
</script>

{#each data.tiles as tile}
    <div style="position: absolute; left: {tile.coords.x}rem; top: {tile.coords.y}rem;">
        {tile.text}
    </div>
{/each}