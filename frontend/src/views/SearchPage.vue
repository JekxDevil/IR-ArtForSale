<template>
  <div class="flex flex-column align-items-center justify-content-center">
    <h1 class="p-5 text-8xl">Art For Sale</h1>
    <div class="w-9 flex text-align-left justify-content-end p-2">
      <label class="p-2">Advanced search</label>
      <InputSwitch v-model="checked" class="p-2"/>
    </div>
    <span v-if="!checked" class="p-input-icon-left w-9 flex align-items-center flex-row justify-content-center">
            <i class="pi pi-search"/>
            <InputText placeholder="Search" class="w-full"/>
    </span>
    <div v-if="checked" class="advancedSearch w-9 flex align-items-center flex-column justify-content-center">
      <div class="flex flex-row w-full justify-content-evenly p-5">
        <div class="flex flex-column w-20rem">
          <label>Keywords</label>
          <span class="p-input-icon-left">
          <i class="pi pi-search"/>
          <InputText placeholder="Keyword" class="w-full"/>
        </span>
        </div>
        <div class="flex flex-column w-20rem">
          <label>Tags</label>
          <span>
          <MultiSelect v-model="selectedTags" :options="tags" :maxSelectedLabels="2" display="chip"
                       placeholder="Selected Tags" class="w-full"></MultiSelect>
        </span>
        </div>

      </div>
      <div class="w-full flex flex-row w-full justify-content-evenly p-5">
        <div class="flex flex-column w-20rem">
          <label>Minimum Price</label>
          <InputNumber v-model="min" inputId="horizontal-buttons" buttonLayout="horizontal" mode="decimal" showButtons
                       :min="0" :max="100" :pt="{input: {class: 'w-1rem'}}"/>
        </div>
        <div class="flex flex-column w-20rem">
          <label>Maximum Price</label>
          <InputNumber v-model="max" inputId="horizontal-buttons" buttonLayout="horizontal" mode="decimal" showButtons
                       :min="0" :max="100" :pt="{input: {class: 'w-1rem'}}"/>
        </div>
      </div>
    </div>
    <div class="results w-9 flex flex-row justify-content-between"
         style="border-top: solid 1px #FFD700">
      <div class="cardsResult flex flex-column justiy-content-center align-items-center">
        <Card v-for="(item, index) in retrievedArt" :key="index" class="w-5 p-10 mt-8" style="border:solid 2px #FFD700 ">
          <template #header>
            <img alt="user header"  style="object-fit:cover; object-position: center"
                 class="w-full max-h-20rem border-round-top" :src="item.img" />
          </template>
          <template #title> {{item.title}} </template>
          <template #subtitle> {{item.author}}, {{item.price}} </template>
          <template #content>
            <p class="m-0">
              {{item.description}}
            </p>
          </template>
          <template #footer>
            <a :href="item.url" target="_blank"><Button icon="pi pi-check" label="Visit Page" :pt="{root: {style: 'bakcground-color: #0013de' }}"/></a>
          </template>
        </Card>
      </div>
      <div class="recomandations flex flex-column justiy-content-center align-items-center">
        Rec
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import {defineComponent, ref, onMounted} from 'vue';
import InputText from "primevue/inputtext";
import InputSwitch from "primevue/inputswitch";
import MultiSelect from "primevue/multiselect";
import InputNumber from "primevue/inputnumber"
import Button from "primevue/button"
import Card from "primevue/card"

const checked = ref(false);
const tags = ref([]);
const selectedTags = ref([]);
const min = ref(0)
const max = ref(1000000000)
const retrievedArt = ref([])

onMounted(() => {
  tags.value = ["Primo", "Secondo", "Terzo"];
  retrievedArt.value = [
    {
      "img": "https://d3rf6j5nx5r04a.cloudfront.net/leW80a3WDJflb56jz-Y4ucl6vKg=/560x0/product/3/9/8a943a83da2d44818d44747ffcd904e9.jpg",
      "author": "Vahe Yeremyan",
      "title": "Abstract Painting Contemporary Original art on Plexiglass One of a kind Framed Ready to Hang Signed with Certificate of Authenticity",
      "price": "£569.39",
      "description": "ARTIST: Vahe Yeremyan",
      "tags": "",
      "url": "https://www.artfinder.com/product/abstract-painting-contemporary-original-art-on-plexiglass-o-cb0c/"
    },
    {
      "img": "https://d3rf6j5nx5r04a.cloudfront.net/lxL_ssd1iTSGdvG600WpLwDaIEA=/560x0/product/9/c/4b7a1ea01a09474099f64e2b2261f4e3_opt.jpg",
      "author": "Adam Mazek",
      "title": "Constructivism (from \"Ostensible abstraction\" set)",
      "price": null,
      "description": "\"Constructivism\" is the thirteenth photograph from \"Ostensible abstraction\" set.*",
      "tags": "",
      "url": "https://www.artfinder.com/product/constructivism-from-ostensible-abstraction-set/"
    },
    {
      "img": "https://d3rf6j5nx5r04a.cloudfront.net/GHmLHgxFNmDg0myd62KgZVRiZPw=/560x0/product/2/a/6ef987dcd9d04048bb0958fd5ba1aec8_opt.jpg",
      "author": "Stephen Brook",
      "title": "Cafe at Tate modern.",
      "price": "£285",
      "description": "Original oil painting of the cafeteria at London’s Tate modern with shaded lighting.",
      "tags": "",
      "url": "https://www.artfinder.com/product/cafe-at-tate-modern-e1f3c/"
    },
    {
      "img": "https://d3rf6j5nx5r04a.cloudfront.net/lyjZ95ziOtJv-d9UrbKl6V7zMcE=/560x0/product/4/1/ffc0daf3464a4bfa9c30db8dc1f34803_opt.jpg",
      "author": "Lucy Moore",
      "title": "Abstract Synapses - I've Never Heard Silence Quite This Loud #2",
      "price": "£1,200",
      "description": "Abstract Synapses - I've Never Heard Silence Quite This Loud #2",
      "tags": "",
      "url": "https://www.artfinder.com/product/abstract-synapses-ive-never-heard-silence-quite-this-loud-2/"
    }
  ];
  console.log(retrievedArt)
});

defineComponent({
  name: 'SearchPage',
});
</script>

<style scoped>
body {
  background-color: #FFFFF0;
}

h1 {
  background: linear-gradient(to bottom right, #0013de, #FFD700);
  -webkit-background-clip: text;
  color: transparent;
}

.p-inputswitch-slider {
  background-color: #0013de;
  color: #0013de
}

.p-button {
  background-color: #0013de;
}
</style>