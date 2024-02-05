<template>
  <div class="m-3 d-flex align-center">
    <a class="fw-bold btn btn-outline-warning" @click.prevent="go_product('deposit')" href="#">예금 조회</a>
    <span class="border-end border-warning m-3" style="height: 20px;"></span>
    <a class="fw-bold btn btn-outline-warning" @click.prevent="go_product('saving')" href="#">적금 조회</a>
    <span class="border-end border-warning m-3" style="height: 20px;"></span>
    <a class="fw-bold btn btn-outline-warning" @click.prevent="go_product('loan')" href="#">대출 조회</a>
  </div>
  <ProductList class="m-3"
    :product-kind="product_kind"
  />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ProductList from '@/components/ProductList.vue'
import { useUserStore } from '@/stores/user'

onMounted(() => {
  store.nowType = 'deposit'
  store.pullBankList()
  store.pullCorperList()
  store.pullProductList_deposit()
  store.pullProductList_saving()
  store.pullProductList_loan()
})

const store = useUserStore()
const product_kind = ref('deposit')

const go_product = function (product) {
  product_kind.value = product
  store.nowType = product
}



</script>

<style scoped>

</style>