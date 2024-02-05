<template>
  <div class="m-3">
    <h1 class="fw-bold mb-3">환율계산기</h1>
    <select class="form-select border-warning mb-5" aria-label="단위 선택" v-model="selectCountry">
      <option v-for="country in store.countries_form" :key="country" :value="country">{{ country }}</option>
    </select>
    <div style="width: 100%; height: 100%;" class="d-flex flex-column align-items-center justify-content-center">
      <h3 class="m-5">실시간 환율을 바로 계산해보세요.</h3>
      <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
        <input type="radio" class="btn-check fw-bold" name="btnradio" id="btnradio1" autocomplete="off" checked @click="toggleConversion('KRWToWon')">
        <label class="btn btn-outline-warning" for="btnradio1">KRW → {{ foreignCurrency }}</label>
        <input type="radio" class="btn-check fw-bold " name="btnradio" id="btnradio2" autocomplete="off" @click="toggleConversion('wonToKRW')">
        <label class="btn btn-outline-warning" for="btnradio2">{{ foreignCurrency }} → KRW</label>
      </div>
      <div v-if="showWonToKRW" class="m-5">
        <div class="d-flex flex-column">
          <div class="d-flex align-items-center">
            <input class="m-0 border border-warning fs-4" type="text" v-model="dollarAmount" @input="convertToWon"/>
            <span class="fs-4 ps-2">{{ foreignCurrency }}</span>
          </div>
          <br>
          <div class="d-flex align-items-center">
            <input class="m-0 border border-warning fs-4" type="text" v-model="wonAmount" @input="convertToDollar"/>
            <span class="fs-4 ps-2">KRW</span>
          </div>
        </div>
      </div>
      <div v-else class="m-5">
        <div class="d-flex flex-column">
          <div class="d-flex align-items-center">
            <input class="m-0 border border-warning fs-4" type="text" v-model="wonAmount" @input="convertToDollar"/>
            <span class="fs-4 ps-2">KRW</span>
          </div>
          <br>
          <div class="d-flex align-items-center">
            <input class="m-0 border border-warning fs-4" type="text" v-model="dollarAmount" @input="convertToWon"/>
            <span class="fs-4 ps-2">{{ foreignCurrency }}</span>
          </div>
        </div>
      </div>
      <p class="fs-6">* 엔화 / 인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const selectCountry = ref("미국 달러 [USD]")
const dollarAmount  = ref(null)
const wonAmount  = ref(null)
const foreignCurrency = ref('USD')
const showWonToKRW = ref(false);

const toggleConversion = (conversionType) => {
  if (conversionType === 'wonToKRW') {
    showWonToKRW.value = true;
  } else {
    showWonToKRW.value = false;
  }
};

let dollarInputActive = false
let wonInputActive = false

const exchangeRate = computed(() => {
  const selectedCurrency = selectCountry.value 
  return store.getExchangeRate(selectedCurrency)
})

const convertToWon = () => {
  const dollarValue = parseInt(dollarAmount.value);
  if (isNaN(dollarValue)) {
    wonAmount.value = null;
    return;
  }

  if (!wonInputActive) {
    const convertedValue = dollarValue * exchangeRate.value;
    wonAmount.value = convertedValue > 0 ? formatValue(convertedValue) : null;
  }
}

const convertToDollar = () => {
  const wonValue = parseInt(wonAmount.value);
  if (isNaN(wonValue)) {
    dollarAmount.value = null;
    return;
  }

  if (!dollarInputActive) {
    const convertedValue = wonValue / exchangeRate.value;
    dollarAmount.value = convertedValue > 0 ? formatValue(convertedValue) : null;
  }
}

const formatValue = (value) => {
  const formattedValue = value.toFixed(2);
  return formattedValue.endsWith('.00') ? value.toFixed(0) : formattedValue;
}

watch(dollarAmount, () => {
  convertToWon()
  dollarInputActive = true
  wonInputActive = false
})

watch(wonAmount, () => {
  convertToDollar()
  wonInputActive = true
  dollarInputActive = false
})

watch(selectCountry, (newVal) => {
  dollarInputActive = false
  wonInputActive = false
  dollarAmount.value = null
  wonAmount.value = null
  const lastThreeChars = newVal.match(/\[(.*?)\]$/)[1]
  foreignCurrency.value = lastThreeChars
})

onMounted(() => {
  store.saveExchangeData()
})
</script>

<style scoped>

</style>