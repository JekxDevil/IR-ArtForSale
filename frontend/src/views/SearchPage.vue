<template>
  <div class="flex flex-column align-items-center justify-content-center">
    <h1 class="p-5 text-8xl">Art For Sale</h1>
    <div class="w-9 flex text-align-left justify-content-end p-2">
    </div>
    <div class="flex flex-column justify-content-center w-full align-items-center">
      <span class="p-input-icon-left w-9 flex align-items-center flex-row justify-content-center">
            <i class="pi pi-search"/>
            <InputText placeholder="Search" v-model="query" class="w-full"/>
        <Button label="Search" class="mt-4 mb-4"  id="searchButton" rounded @click="mymethod(query)" @keyup.enter="mymethod(query)"></Button>
    </span>
    </div>
    <div class="advancedSearch w-9 flex align-items-start flex-column justify-content-start" v-if="filterVisible">
      <h4>Filters</h4>
      <div class="flex flex-row w-full justify-content-start gap-2 pb-2">
        <div>

          <span class="p-float-label">
          <MultiSelect v-model="selectedSites" :options="sites" :maxSelectedLabels="2" display="chip"
                       placeholder="Selected Tags" class="w-full"></MultiSelect>
            <label>Site of origin</label>
        </span>
        </div>
        <div>

          <span class="p-float-label">
          <MultiSelect v-model="selectedTags" :options="tags" :selectionLimit="1" :maxSelectedLabels="2" display="chip"
                       placeholder="Selected Tags" class="w-full"></MultiSelect>
            <label>Tags</label>
        </span>
        </div>

        <div>
          <span class="p-float-label">

          <InputNumber v-model="min" inputId="horizontal-buttons" mode="decimal"
                       :min="0" :max="100000000" :pt="{input: {class: 'w-10rem'}}"/>
            <label>Minimum Price</label>
          </span>
        </div>
        <div>
          <span class="p-float-label">
          <InputNumber v-model="max"  mode="decimal"
                       :min="0" :max="100000000"   :pt="{input: {class: 'w-10rem'}}"/>
          <label>Maximum Price</label>
            </span>
        </div>
        <Button label="Filter" icon="pi pi-filter" @click="filterByPriceRange(min, max, selectedSites, selectedTags)"></Button>
      </div>
    </div>
    <div class="card flex justify-content-center">
      <Sidebar v-model:visible="visibleBar" position="right" class="w-auto">
        <div class="flex flex-column justify-content-center align-items-center">
          <h1>Based on the tags of these paintings</h1>
          <h1>You might also like</h1>
          <div v-for="(item, index) in suggestions" :key="index">
            <div class="flex flex-column justify-content-center align-items-center" v-if="item.length != 0">
              <h2>{{complete_tags[index]}}</h2>
              <Carousel :value="spliceItem(item)" circular :num-scroll="1" :responsiveOptions="responsiveOptions" class="w-25rem h-full"   :autoplayInterval="3000" >
                <template #item="slotProps">
                  <div class="border-1 surface-border border-round m-2 text-center py-5  px-3" style="height:500px">
                    <div class="mb-3">
                      <img :src="slotProps.data.image" :alt="slotProps.data.title" class="w-full max-h-20rem border-round-top" style="object-fit:cover; object-position: center; height:200px"/>
                    </div>
                    <div>
                      <h4 class="mb-1">{{ trimString(slotProps.data.title, 30) }}</h4>
                      <p class="mt-0 mb-3">{{ slotProps.data.price }}</p>
                      <Tag v-for="(tag, index) in trimTags(slotProps.data.tags)" v-if="index < 5" :key="index" :value="trimString(tag, 10)" class="p-1 ml-1" rounded></Tag>
                      <div class="mt-5 flex align-items-center justify-content-center gap-2">
                        <a :href="slotProps.data.url" target="_blank"><Button icon="pi pi-check" label="Visit Page" :pt="{root: {style: 'bakcground-color: #0013de' }}"/></a>
                      </div>
                    </div>
                  </div>
                </template>
              </Carousel>
            </div>
          </div>
        </div>
      </Sidebar>
      <Button icon="pi pi-arrow-right" label="See some recommendation"  v-if="filteredValues.length != 0" class="mt-2 mb-2" @click="visibleBar = true" />
    </div>
    <div class="results w-9 flex flex-column justify-content-between"
         style="border-top: solid 1px #FFD700">
      <div class="cardsResult flex flex-row flex-wrap justify-content-center align-items-center gap-5">
        <Card v-for="(item, index) in filteredValues" :key="index" class="w-3 p-10 mt-8" style="box-shadow: 0px 0px 15px 12px #646464; height: 600px ">
          <template #header>
            <img alt="user header"  style="object-fit:cover; height:200px; object-position: center"
                 class="w-full max-h-20rem border-round-top"  :src="item.image" />
          </template>
          <template #title> {{trimString(item.title, 30)}} </template>
          <template #subtitle> {{item.author}}, {{item.price}} </template>
          <template #content>
            <p class="m-0">
              {{trimString(item.description, 60)}}
            </p>
            <Tag v-for="(tag, index) in trimTags(item.tags)" :key="index" :value="trimString(tag, 10)" class="p-1 mr-1 mt-5" rounded></Tag>
          </template>
          <template #footer>
            <a :href="item.url" target="_blank"><Button icon="pi pi-check" label="Visit Page" :pt="{root: {style: 'bakcground-color: #0013de' }}"/></a>

          </template>
        </Card>
      </div>
      <Dialog v-model:visible="visible" modal header="Error" :style="{ width: '50rem' }" class="flex flex-column  justify-content-center" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
        <p class="text-2xl flex justify-content-center flex-column text-align-center">
          Your query:<br>
          <p><b>{{query}}</b></p>
          <p>Has given no results</p>
        </p>
      </Dialog>
    </div>
  </div>
</template>
<script setup lang="ts">
import {defineComponent, ref, onMounted} from 'vue';
import {useDocumentStore} from '@/stores/document';
import InputText from "primevue/inputtext";
import InputSwitch from "primevue/inputswitch";
import MultiSelect from "primevue/multiselect";
import InputNumber from "primevue/inputnumber"
import Button from "primevue/button"
import Card from "primevue/card"
import Carousel from "primevue/carousel"
import Tag from 'primevue/tag';
import Dialog from "primevue/dialog";
import Sidebar from "primevue/sidebar";

const tags = ref([]);
const sites = ref(["Artsy", "Saatchi", "ArtFinder"])
const selectedSites = ref([])
const selectedTags = ref([]);
const min = ref(0)
const max = ref(1000000000)
const retrievedArt = ref([])
const query = ref('');
const suggestions = ref([])
const filteredValues = ref([])
const complete_tags = ref([])
const filterVisible = ref(false)
const visible = ref(false)
const visibleBar = ref(false)
const responsiveOptions = ref([
  {
    breakpoint: '1400px',
    numVisible: 2,
    numScroll: 1
  },
  {
    breakpoint: '1199px',
    numVisible: 3,
    numScroll: 1
  },
  {
    breakpoint: '767px',
    numVisible: 2,
    numScroll: 1
  },
  {
    breakpoint: '575px',
    numVisible: 1,
    numScroll: 1
  }
]);



const trimString = (desc, qt) => {
  if(desc.length > qt) {
    return desc.substring(0, qt) + "..."
  }
  return desc
}

const trimTags = (desc) => {
  if(desc == null) {
    return ""
  }
  if(desc.length > 5) {
    return desc.slice(0, 5)
  }
  return desc
}



const mymethod = async (q: string) => {
  const documentStore = useDocumentStore();
  await documentStore.getDocuments(q);
  retrievedArt.value = documentStore.documents
  console.log(retrievedArt)
  if(retrievedArt.value.length == 0) {
    console.log("TEL CHI")
    visible.value = true
    console.log("VI",visible)
  }
  filteredValues.value = documentStore.documents
  min.value = 0
  max.value = 1000000
  selectedSites.value = []
  selectedTags.value = []
  getAllTags()
  filterVisible.value = true
  await documentStore.getRecomended({tags: complete_tags.value})
  suggestions.value = documentStore.recomandations
}

const getAllTags = () => {
  let all_tags = [];
  for (const item of retrievedArt.value) {
    if(item.tags !== null && item.tags !== undefined) {
      all_tags = all_tags.concat(item.tags.map((element) => {return element.toLowerCase()}));
    }

  }
  console.log(query)
  const query_array = query.value.split(" ");
  const cleaned_tags = all_tags.filter( function( el ) {
    return !query_array.includes( el );
  } );
  complete_tags.value = findTop3Tag(cleaned_tags)
  tags.value = all_tags.filter((value, index) => all_tags.indexOf(value) === index);
};

const spliceItem = (arr) => {
  if(arr.length > 5) {
    console.log("ECCOMI")
    return arr.slice(0, 5)
  }
  return arr
}
const findTop3Tag = (arr)  =>{
  const countMap = {};

  arr.forEach(str => {
    countMap[str] = (countMap[str] || 0) + 1;
  });

  const countArray = Object.entries(countMap).map(([key, value]) => ({ key, value }));

  countArray.sort((a, b) => b.value - a.value);

  return countArray.slice(0, 5).map(entry => entry.key);

}

const filterByPriceRange = (minPrice, maxPrice, siteToFilter, tagToFilter) => {
  console.log("SITES", siteToFilter);
  console.log("selected", selectedSites)
  if(!Array.isArray(siteToFilter)) {
    siteToFilter = []
  }

  const filteredResults = retrievedArt.value.filter(item => {
    if (item.price !== null && item.price !== undefined) {
      const numericPrice = parseFloat(item.price.replace(/[^0-9.]/g, ''));
      const priceInRange = numericPrice >= minPrice && numericPrice <= maxPrice;
      let siteInUrl = true
      console.log(siteToFilter)
      if(siteToFilter.length != 0) {
        siteInUrl = siteToFilter.some(word => item.url.includes(word.toLowerCase()));
      }
      let tagInArt = true
      if(tagToFilter.length == 1) {
        let item_tag = item.tags || [];
        tagInArt = item_tag.includes(tagToFilter[0])
      }


      return priceInRange && siteInUrl && tagInArt;
    }
    return false;
  });
  console.log("FILTERED", filteredResults)
  filteredValues.value = filteredResults
};

defineComponent({
  name: 'SearchPage',
});
</script>

<style scoped>
body {
  background-color: #FFFFF0;
}

h1 {
  background: rgb(212,175,55);
  background: linear-gradient(349deg, rgba(212,175,55,1) 27%, rgba(20,40,208,1) 94%);
  -webkit-background-clip: text;
  color: transparent;
}
.p-tag {
  background-color: #5565f5
}

.p-inputswitch-slider {
  background-color: #0013de;
  color: #0013de
}

.p-button, .p-carousel-indicator  {
  background-color: #5565f5;
}
</style>