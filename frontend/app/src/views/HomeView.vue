<template>
  <main class=" container flex h-screen w-full flex-col items-center justify-center gap-24 text-high-contrast-text dark:text-d-high-contrast-text">
    <h1 class=" text-5xl font-black">Ultimate Rubik's Cube Solver</h1>

    <div class="flex w-full flex-row items-center justify-around">

      <!-- Colors Palette -->
      <div class="flex w-1/6 flex-col items-center justify-center gap-4">
        <div class=" color-choose bg-white"></div>
        <div class=" color-choose bg-red-500"></div>
        <div class=" color-choose bg-orange-400"></div>
        <div class=" color-choose bg-yellow-300"></div>
        <div class=" color-choose bg-green-400"></div>
        <div class=" color-choose bg-blue-500"></div>
      </div>

      <!-- Canvas -->
      <!-- <div class="w-1/3 "> -->
        <div class=" size-96 bg-black/20">
        </div>
      <!-- </div> -->

      <!-- Movements -->
       <div class="flex w-1/6 justify-center">
         <div class="grid w-fit grid-cols-2 gap-4">
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
      <div class="flex flex-row justify-center gap-6">
        <input type="text" placeholder="Enter a sequence" class="sequence-input">
        <div class="icon-button"><ClipboardIcon/></div>
        <div class="icon-button"><PlayIcon/></div>
      </div>
      <div class="flex w-full flex-row justify-between">
        <div class="icon-button"><DeleteIcon/></div>
        <div class="icon-button"><AutorenewIcon/></div>
        <div class="icon-button"><ShuffleIcon/></div>
        <div class="text-button">SOLVE</div>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import AutorenewIcon from '@/assets/radixIcons/AutorenewIcon.vue';
import ClipboardIcon from '@/assets/radixIcons/ClipboardIcon.vue';
import DeleteIcon from '@/assets/radixIcons/DeleteIcon.vue';
import PlayIcon from '@/assets/radixIcons/PlayIcon.vue';
import ShuffleIcon from '@/assets/radixIcons/ShuffleIcon.vue';



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
