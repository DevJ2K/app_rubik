<template>
	<div class="neumorphism-md relative flex w-3/4 min-w-80 flex-col rounded-2xl p-4 text-lg">

		<!-- <div class="absolute right-0 top-0 mr-4 mt-4 cursor-pointer"  @click="$emit('display-modal')">
			<InfoIcon size="size-5"/>
		</div> -->

		<h1 class=" font-extrabold text-red-500">{{ title }}</h1>
		<p class=" font-normal text-red-500">{{ description }}</p>
	</div>
</template>

<script setup lang="ts">
// import InfoIcon from '@/assets/Svg/InfoIcon.vue';

defineProps({
	title: {
		type: String,
		default: 'Informations'
	},
	description: {
		type: String,
		default: 'No information.'
	}
});

</script>

<style scoped>

</style>
