<template>
  <div>
    <!-- 예금 조회 -->
    <div v-if="productKind === 'deposit'">
      <h1 class="fw-bold">예금 조회</h1>
      <select class="form-select border-warning mb-1" aria-label="은행 선택" v-model="selectedBank_deposit">
        <option v-for="(bank, index) in store.banks" :key="index" :value="bank">{{ bank }}</option>
      </select>
      <select class="form-select border-warning mb-1" aria-label="예치 기간 선택" v-model="selectedPeriod_deposit">
        <option v-for="(period, index) in periods" :key="index" :value="period">{{ period }}</option>
      </select>
      <button class="btn btn-warning" @click.prevent="searchDeposit">확인</button>
      
    </div>
    
    <!-- 적금 조회 -->
    <div v-if="productKind === 'saving'">
      <h1 class="fw-bold">적금 조회</h1>
      <select class="form-select border-warning mb-1" aria-label="은행 선택" v-model="selectedBank_saving">
        <option v-for="(bank, index) in store.banks" :key="index" :value="bank">{{ bank }}</option>
      </select>
      <select class="form-select border-warning mb-1" aria-label="예치 기간 선택" v-model="selectedPeriod_saving">
        <option v-for="(period, index) in periods" :key="index" :value="period">{{ period }}</option>
      </select>
      <button class="btn btn-warning" @click.prevent="searchDeposit">확인</button>
    </div>
    
    <!-- 대출 조회 -->
    <div v-if="productKind === 'loan'">
      <h1 class="fw-bold">대출 조회</h1>
      <select class="form-select border-warning mb-1" aria-label="은행 선택" v-model="selectedBank_loan">
        <option v-for="(product, index) in store.corpers" :key="index" :value="product">{{ product }}</option>
      </select>
      <select class="form-select border-warning mb-1" aria-label="담보 선택" v-model="selectedPeriod_loan">
        <option v-for="(security, index) in securities" :key="index" :value="security">{{ security }}</option>
      </select>
      <button class="btn btn-warning" @click.prevent="searchDeposit">확인</button>      
    </div>

    <ProductListItem 
      :product-kind="productKind"
    />
  </div>
  
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import ProductListItem from '@/components/ProductListItem.vue' 
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const props = defineProps({
  productKind: String
})

const periods = ref(['전체 선택', '6개월', '12개월', '24개월', '36개월'])
const securities = ref(['전체 선택', '고정금리', '변동금리'])
const selectedBank_deposit = ref('전체 선택')
const selectedPeriod_deposit = ref('전체 선택')
const selectedBank_saving = ref('전체 선택')
const selectedPeriod_saving = ref('전체 선택')
const selectedBank_loan = ref('전체 선택')
const selectedPeriod_loan = ref('전체 선택')

watch(() => props.productKind, () => {
  if (props.productKind === 'deposit') {
    store.searchDeposit('전체 선택', '전체 선택', props.productKind)
    selectedBank_deposit.value = '전체 선택'
    selectedPeriod_deposit.value = '전체 선택'
  } else if (props.productKind === 'saving') {
    store.searchDeposit('전체 선택', '전체 선택', props.productKind)
    selectedBank_saving.value = '전체 선택'
    selectedPeriod_saving.value = '전체 선택'
  } else {
    store.searchDeposit('전체 선택', '전체 선택', props.productKind)
    selectedBank_loan.value = '전체 선택'
    selectedPeriod_loan.value = '전체 선택'    
  }
})

const searchDeposit = function () {
  if (props.productKind === 'deposit') {
    store.searchDeposit(selectedBank_deposit.value, selectedPeriod_deposit.value, props.productKind)
  } else if (props.productKind === 'saving') {
    store.searchDeposit(selectedBank_saving.value, selectedPeriod_saving.value, props.productKind)
  } else {
    store.searchDeposit(selectedBank_loan.value, selectedPeriod_loan.value, props.productKind)
  }
}

</script>

<style>

</style>