<template>
  <main class=" text-high-contrast-text container my-12 flex size-full flex-col items-center justify-center gap-24">
    <div class=" flex w-full flex-col items-center justify-center gap-6">
      <h1 class="text-3xl font-bold">Project name</h1>
      <p class=" text-low-contrast-text text-center">Est nulla ea do nulla qui. Do minim eiusmod laboris ea nostrud eu consequat aliqua. Reprehenderit et nisi tempor cupidatat cupidatat nisi tempor occaecat aliquip et. Cupidatat labore sint ipsum magna ut dolore sit duis qui dolore esse. Fugiat enim id nulla qui. Laborum aute culpa qui nisi aliquip minim aliquip. Eiusmod dolore culpa laborum cillum officia esse fugiat Lorem nisi amet est labore et. Dolore commodo aliqua mollit cupidatat ex veniam quis sit non cupidatat exercitation fugiat amet. Dolore cillum labore excepteur culpa labore ea qui id sunt in magna ad nisi veniam.</p>
      <div class="flex h-40 w-full flex-col gap-2 md:flex-row">
        <div class="border-ui-border h-full rounded-md border-4 bg-black md:w-1/3">

        </div>
        <div class="border-ui-border h-full rounded-md border-4 bg-black md:w-1/3">

        </div>
        <div class="border-ui-border h-full rounded-md border-4 bg-black md:w-1/3">

        </div>
      </div>
    </div>

    <div class="flex w-full flex-col items-center justify-center gap-6">
      <h1 class="text-2xl font-bold">Test Overview</h1>
      <p class=" text-low-contrast-text text-center">Excepteur fugiat excepteur occaecat sint id reprehenderit excepteur nulla non ipsum. Pariatur aute sunt laboris tempor proident proident exercitation ad nisi deserunt sit dolor labore. Enim consectetur est est non id veniam aliquip elit exercitation. Ex aliqua duis enim incididunt incididunt.</p>
    </div>

    <div class="flex w-full flex-col items-center justify-center gap-6">
      <h1 class="text-2xl font-bold">Test Execution</h1>
      <div class="flex w-full flex-col items-center justify-center gap-3">
        <label for="test-input">Lorem ipsum :</label>
        <input type="text" id="test-input" required class="form-input form-input-border w-5/6">
        <button @click="makeRequests"
							class="border-accent-color text-high-contrast-text hover:bg-accent-color dark:text-d-high-contrast-text group flex flex-row items-center gap-1.5 rounded-full border-2 px-6 py-2 transition-colors">
							<span class=" font-semibold transition-colors group-hover:text-white">Submit</span>
					</button>
      </div>
      <div>
        <h1 class=" text-xl font-semibold">API Result</h1>

        <p id="api_result"></p>
      </div>
    </div>
    <!-- <TheWelcome /> -->
  </main>
</template>

<script setup lang="ts">

const makeRequests = async () => {
  console.log("Yo !");
  const input: HTMLElement | null = document.getElementById("test-input");

  let text: String = '';
  if (input) {
    text = input.value;
  }
  const url = "http://127.0.0.1:4000/test";

  try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({name: text}),
        });

        const result = await response.json();
        console.log("Response from FastAPI:", result);
        const api_result = document.getElementById("api_result");
        if (api_result) {
          api_result.innerHTML = result.message;
        }
    } catch (error) {
        console.error("Error:", error);
    }
};

</script>
