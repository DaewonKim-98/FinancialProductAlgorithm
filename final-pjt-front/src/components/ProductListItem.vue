<template>
  <div class="border border-warning mt-2">
    <v-data-table class="border-warning"
      :items="productList"
      :headers="dynamicHeaders"
      :items-per-page="10"
      @click:row="go_detail"
    ></v-data-table>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const props = defineProps({
  productKind: String
})

const store = useUserStore()
const productList = ref(store.productList_deposit)

watch(() => store.searchProduct, (newVal, oldVal) => {
  productList.value = newVal
})


const dynamicHeaders = computed(() => {
  if (props.productKind === 'loan') {
    return [
      {
        title: '회사명',
        value: 'kor_co_nm',
        sortable: true
      },
      {
        title: '상품명',
        value: 'fin_prdt_nm',
        sortable: true
      },
      {
        title: '고정금리 (최소)',
        value: '고정금리',
        sortable: true
      },
      {
        title: '변동금리 (최소)',
        value: '변동금리',
        sortable: true
      },
    ]
  } else {
    return [
      {
        title: '회사명',
        value: 'kor_co_nm',
        sortable: true
      },
      {
        title: '상품명',
        value: 'fin_prdt_nm',
        sortable: true
      },
      {
        title: '6개월',
        value: '6',
        sortable: true
      },
      {
        title: '12개월',
        value: '12',
        sortable: true
      },
      {
        title: '24개월',
        value: '24',
        sortable: true
      },
      {
        title: '36개월',
        value: '36',
        sortable: true
      },
    ]
  }
})

const go_detail = function(event, { item }) {
  router.push({ name: 'productDetail', params: { id: item.fin_prdt_cd } })
}

</script>

<style scoped>

</style>