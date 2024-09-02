<template>
	<div class=" fixed top-0 z-50 w-full">
		<div id="navBar" class="my-scroll-nav my-scroll-nav-active">
			<div id="navMenu"
				class="absolute top-0 h-screen w-full -translate-x-full transition-transform duration-500 md:hidden">
				<ul
					class=" bg-app-bg text-high-contrast-text dark:bg-d-app-bg dark:text-d-high-contrast-text flex size-full flex-col items-center justify-center gap-14 py-4 text-xl font-semibold">

					<li class="group relative w-max">
						<p @click="routerTo('/')"
							class="cursor-pointer transition-all group-hover:text-black dark:group-hover:text-white">
							Home</p>
						<span class="animate-underline"></span>

					</li>
					<li class="group relative w-max">
						<p @click="routerTo('/page1')"
							class="cursor-pointer transition-all group-hover:text-black dark:group-hover:text-white">
							Page 1</p>
						<span class="animate-underline"></span>

					</li>
					<li class="group relative w-max">
						<p @click="routerTo('/page2')"
							class="cursor-pointer transition-all group-hover:text-black dark:group-hover:text-white">
							Page 2</p>
						<span class="animate-underline"></span>

					</li>
					<a :href="downloadLink" target="_blank"
							class="border-accent-color text-high-contrast-text hover:bg-accent-color dark:text-d-high-contrast-text group flex flex-row items-center gap-1.5 rounded-full border-2 px-6 py-2 transition-colors">
							<DownloadSvg svg-class="text-high-contrast-text size-5 group-hover:text-white transition-colors"/>
							<span class=" font-semibold transition-colors group-hover:text-white">Download</span>
					</a>
				</ul>
			</div>

			<div class=" container flex items-center justify-between md:justify-center">
				<div class="flex w-1/3 justify-start">
					<div @click="routerTo('/')" class=" flex cursor-pointer flex-row items-center gap-4">
						<div class=" size-16 overflow-hidden rounded-full border-2 bg-blue-50">
							<img src="../../assets/images/j2klogo.png" alt="" class=" size-full object-cover">
						</div>
						<h1 id="devj2kText" class="text-outline text-2xl font-black text-transparent">DevJ2K</h1>
					</div>
				</div>
				<ul
					class=" text-high-contrast-text dark:text-d-high-contrast-text flex w-1/3 flex-row items-center justify-center gap-8 text-lg font-semibold max-md:hidden">
					<li class="group relative w-max">
						<p @click="routerTo('/')"
							class="cursor-pointer transition-all group-hover:text-black dark:group-hover:text-white">
							Home</p>
						<span class="animate-underline"></span>

					</li>
					<li class="group relative w-max">
						<p @click="routerTo('/page1')"
							class="cursor-pointer transition-all group-hover:text-black dark:group-hover:text-white">
							Page 1</p>
						<span class="animate-underline"></span>

					</li>
					<li class="group relative w-max">
						<p @click="routerTo('/page2')"
							class="cursor-pointer transition-all group-hover:text-black dark:group-hover:text-white">
							Page 2</p>
						<span class="animate-underline"></span>

					</li>
				</ul>
				<div class=" flex w-1/3 justify-end max-md:hidden">
					<a :href="downloadLink" target="_blank"
						class="border-accent-color text-high-contrast-text hover:bg-accent-color dark:text-d-high-contrast-text group flex flex-row items-center gap-1.5 rounded-full border-2 px-6 py-2 transition-colors">
						<DownloadSvg svg-class="text-high-contrast-text size-5 group-hover:text-white transition-colors"/>
						<span class=" font-semibold transition-colors group-hover:text-white">Download</span>
					</a>
				</div>

				<div class="z-[1] size-fit cursor-pointer md:hidden" @click="toggleMenu">
					<NavHamburger />
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">

import { ref } from 'vue';
import NavHamburger from '../NavHamburger.vue';
import { useRouter } from 'vue-router';
import DownloadSvg from '../svg/DownloadSvg.vue';

const displayMenu = ref(false);
const router = useRouter();
const downloadLink = downloadProject;

const toggleMenu = () => {

	const bar1 = document.getElementById('hamburger-bar-1');
	const bar2 = document.getElementById('hamburger-bar-2');
	const bar3 = document.getElementById('hamburger-bar-3');
	const navMenu = document.getElementById('navMenu');
	displayMenu.value = !displayMenu.value;

	if (bar1) {
		// Bar 1
		bar1.classList.toggle('rotate-45', displayMenu.value);
		bar1.classList.toggle('translate-y-2.5', displayMenu.value);
	}
	if (bar2) {
		// Bar 2
		bar2.classList.toggle('scale-x-0', displayMenu.value);
	}
	if (bar3) {
		// Bar 3
		bar3.classList.toggle('-rotate-45', displayMenu.value);
		bar3.classList.toggle('-translate-y-2.5', displayMenu.value);
	}
	if (navMenu) {
		navMenu.classList.toggle('-translate-x-full', !displayMenu.value);
	}
}

// const navigateTo = (id: string, hideMenu = true) => {
// 	if (hideMenu && displayMenu.value == true) {
// 		toggleMenu();
// 	}
// 	// console.log('Go to : ' + id);
// 	const view = document.getElementById(id);
// 	if (view != null) {
// 		view.scrollIntoView({
// 			behavior: 'smooth'
// 		});
// 	}
// }

const routerTo = (link: String, hideMenu = true) => {
	if (hideMenu && displayMenu.value == true) {
		toggleMenu();
	}
	router.push(`${link}`);
}

</script>
