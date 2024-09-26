<template>
	<div class="neumorphism-md relative flex w-3/4 min-w-80 flex-col rounded-2xl p-4 text-lg">

		<div class="absolute right-0 top-0 mr-4 mt-4 cursor-pointer"  @click="$emit('display-modal')">
			<InfoIcon size="size-5"/>
		</div>

		<h1 class=" font-extrabold">Move {{ current_moves }} of {{ nb_moves }}</h1>
		<p class=" font-normal">{{ description }}</p>
	</div>
</template>

<script setup lang="ts">
import InfoIcon from '@/assets/Svg/InfoIcon.vue';

defineEmits(["display-modal"]);
defineProps({
	moves: {
		type: Array<any>,
		default: [
			{

			}
		]
	},
	current_moves: {
		type: Number,
		default: 2
	},
	nb_moves: {
		type: Number,
		default: 20
	},
	description: {
		type: String,
		default: 'Press play button to run the animation.'
	}
});

</script>

<style scoped>

</style>
