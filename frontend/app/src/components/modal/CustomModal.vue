<template>
	<Teleport to="body">
		<Transition name="modal-outer">
			<div v-show="modalActive"
				class="fixed left-0 top-0 flex h-screen w-full items-center justify-center bg-black/60 px-8">
				<Transition name="modal-inner">
					<div v-if="modalActive" class=" w-screen max-w-screen-sm rounded-2xl bg-ui-bg p-4 dark:bg-d-ui-bg">
						<div class="flex w-full justify-end">
							<button @click="$emit('close-modal')"><CloseIcon size="size-6"/></button>
						</div>
						<slot />
					</div>
				</Transition>
			</div>
		</Transition>
	</Teleport>
</template>

<script setup lang="ts">
import CloseIcon from '@/assets/Svg/CloseIcon.vue';

defineEmits(["close-modal"]);
defineProps({
	modalActive: {
		type: Boolean,
		default: false
	}
});

</script>

<style scoped>
.modal-outer-enter-active,
.modal-outer-leave-active {
	transition: opacity 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}
.modal-outer-enter-from,
.modal-outer-leave-to {
	opacity: 0;
}

.modal-inner-enter-active {
	transition: all 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02) 0.15s;
}

.modal-inner-leave-active {
	transition: all 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-inner-enter-from {
	opacity: 0;
	transform: scale(0.8);
}
.modal-inner-leave-to {
	transform: scale(0.8);
}
</style>
