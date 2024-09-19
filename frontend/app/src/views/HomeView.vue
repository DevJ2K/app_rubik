<template>
  <main class=" container flex min-h-screen w-full flex-col items-center justify-center gap-16 text-high-contrast-text dark:text-d-high-contrast-text md:gap-24">
    <h1 class=" text-center text-2xl font-black sm:text-3xl md:text-5xl">Ultimate Rubik's Cube Solver</h1>

    <div class="flex w-full flex-col items-center justify-around gap-8 md:flex-row md:gap-0">

      <!-- Colors Palette -->
      <div class="flex flex-row items-center justify-center gap-4 max-md:order-2 md:w-1/6 md:flex-col">
        <div class=" color-choose bg-white"></div>
        <div class=" color-choose bg-red-500"></div>
        <div class=" color-choose bg-orange-400"></div>
        <div class=" color-choose bg-yellow-300"></div>
        <div class=" color-choose bg-green-400"></div>
        <div class=" color-choose bg-blue-500"></div>
      </div>

      <!-- Canvas -->
      <!-- <div class="w-1/3 "> -->
        <div class=" size-96 bg-black/20 max-md:order-1">
        </div>
      <!-- </div> -->

      <!-- Movements -->
      <div class="flex justify-center max-md:order-3 md:w-1/6">
        <div class="grid w-fit grid-cols-6 gap-4 md:grid-cols-2">
          <div class="movements">U</div>
          <div class="movements">U'</div>
          <div class="movements">D</div>
          <div class="movements">D'</div>
          <div class="movements">F</div>
          <div class="movements">F'</div>
          <div class="movements">B</div>
          <div class="movements">B'</div>
          <div class="movements">L</div>
          <div class="movements">L'</div>
          <div class="movements">R</div>
          <div class="movements">R'</div>
        </div>
      </div>
    </div>



    <div class="flex flex-col gap-8">
      <div class="hidden flex-row justify-center gap-6 sm:flex">
        <input type="text" placeholder="Enter a sequence" class="sequence-input">
        <div class="icon-button"><ClipboardIcon/></div>
        <div class="icon-button"><PlayIcon/></div>
      </div>
      <div class="grid w-full grid-cols-3 flex-row justify-between max-sm:gap-6 sm:flex">
        <div class="icon-button"><DeleteIcon/></div>
        <div class="icon-button"><AutorenewIcon/></div>
        <div class="icon-button" @click="toggleGeneratorModal"><ShuffleIcon/></div>
        <div class="text-button col-span-3 max-sm:py-3">SOLVE</div>
      </div>
    </div>
  </main>

  <GeneratorModal :modal-active="generatorModalActive" @close-modal="toggleGeneratorModal">

    <h1 class="text-center text-lg font-extrabold text-high-contrast-text dark:text-d-high-contrast-text">Mixing Generator Settings</h1>

    <div class="flex w-full flex-col items-start gap-4 py-5">
      <label id="range_nb_moves_label" for="range_nb_moves" class="subtitle-modal">Number of Moves : 1</label>
      <div class="relative w-full">
        <input id="range_nb_moves" @input="updateRangeText('range_nb_moves_label', 'Number of Moves : ' + $event.target.value)" class="custom-range-input" type="range" min="1" max="10" value="1">
      </div>
    </div>

    <div class="flex w-full flex-col items-start gap-4 py-5">
      <label id="range_nb_mixes_label" for="range_nb_mixes" class="subtitle-modal">Number of Mixes : 1</label>
      <div class="relative w-full">
        <input id="range_nb_mixes" @input="updateRangeText('range_nb_mixes_label', 'Number of Mixes : ' + $event.target.value);" class="custom-range-input" type="range" min="1" max="10" value="1">
      </div>
    </div>

    <div class="mb-4 mt-6 flex w-full items-center justify-center">
      <button class="text-button py-2 text-high-contrast-text dark:text-d-high-contrast-text">GENERATE MIX</button>
    </div>

  </GeneratorModal>
</template>

<script setup lang="ts">
import AutorenewIcon from '@/assets/Svg/AutorenewIcon.vue';
import ClipboardIcon from '@/assets/Svg/ClipboardIcon.vue';
import DeleteIcon from '@/assets/Svg/DeleteIcon.vue';
import PlayIcon from '@/assets/Svg/PlayIcon.vue';
import ShuffleIcon from '@/assets/Svg/ShuffleIcon.vue';
import GeneratorModal from '../components/modal/GeneratorModal.vue';
import { onMounted, ref } from 'vue';

const generatorModalActive = ref(true);

const toggleGeneratorModal = () => {
  generatorModalActive.value = !generatorModalActive.value;
}

function updateRangeText(labelId: string, text: string) {
  const labelHtml = document.getElementById(labelId);
  if (!labelHtml) { return; }
  labelHtml.textContent = text;
}

onMounted(() => {});

// const makeRequests = async () => {
//   console.log("Yo !");
//   const input: HTMLElement | null = document.getElementById("test-input");

//   let text: String = '';
//   if (input) {
//     text = input.value;
//   }
//   const url = "http://127.0.0.1:4000/test";

//   try {
//         const response = await fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({name: text}),
//         });

//         const result = await response.json();
//         console.log("Response from FastAPI:", result);
//         const api_result = document.getElementById("api_result");
//         if (api_result) {
//           api_result.innerHTML = result.message;
//         }
//     } catch (error) {
//         console.error("Error:", error);
//     }
// };

</script>
