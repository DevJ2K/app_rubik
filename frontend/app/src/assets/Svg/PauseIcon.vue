<template>


	<svg :class="[color, size]" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="currentColor"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
	</template>

	<script setup lang="ts">
	defineProps({
		color: {
			type: String,
			default: 'text-white'
		},
		size: {
			type: String,
			default: 'w-4 h-4'
		}
	});
	</script>

	<style scoped>

	</style>
