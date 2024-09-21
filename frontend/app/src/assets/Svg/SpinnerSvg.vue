<template>
	<svg
		:class="[custom]"
		fill="none"
		xmlns="http://www.w3.org/2000/svg"
		viewBox="0 0 100 100"
		preserveAspectRatio="xMidYMid"
		width="200"
		height="200"
		xmlns:xlink="http://www.w3.org/1999/xlink"
		style="shape-rendering:auto;display:block;background-position-x:0%;background-position-y:0%;background-size:auto;background-origin:padding-box;background-clip:border-box;background:scroll none repeat;"
	>
		<circle
		:stroke="strokeColor"
		stroke-dasharray="164.93361431346415 56.97787143782138"
		r="35"
		stroke-width="10"
		fill="none"
		cy="50"
		cx="50"
		transform="matrix(1,0,0,1,0,0)"
		style="fill:none;stroke:currentColor;transform:matrix(1, 0, 0, 1, 0, 0);"
		></circle>
	</svg>
	</template>

	<script setup lang="ts">
	defineProps({
	custom: {
		type: String,
		default: 'text-blue-500 size-14'
	},
	strokeColor: {
		type: String,
		default: '#ff00ff'  // Default color if not specified
	}
	});
	</script>


