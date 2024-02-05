import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import VCalendar from 'v-calendar'
import 'v-calendar/style.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { MonthPicker } from 'vue-month-picker'
import { MonthPickerInput } from 'vue-month-picker'

const app = createApp(App)
const pinia = createPinia()
const vuetify = createVuetify({
  components,
  directives,
})

pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.use(router)
app.use(vuetify)
app.use(VCalendar)
app.use(MonthPicker)
app.use(MonthPickerInput)

app.mount('#app')

