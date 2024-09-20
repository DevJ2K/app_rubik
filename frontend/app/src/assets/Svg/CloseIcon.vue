<template>
	<svg :class="[color, size]" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="m259-174-84-85 220-221-220-221 84-85 221 221 221-221 84 85-220 221 220 221-84 85-221-221-221 221Z"/></svg>
</template>

<script setup lang="ts">
defineProps({
	color: {
		type: String,
		default: 'text-white'
	},
	size: {
		type: String,
		default: 'w-5 h-5'
	}
});
</script>

<style scoped></style>
