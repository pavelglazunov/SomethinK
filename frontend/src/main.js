import {createApp} from 'vue'
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'
import MainPage from "@/views/MainPage";
import AuthPage from "@/views/AuthPage";

const router = createRouter({
    routes: [{
        path: "/",
        name: "home",
        component: MainPage
    },
        {
           path: "/auth",
           name: "auth",
           component: AuthPage
        }

    ],
    history: createWebHistory()
})

const app = createApp(App)
app.use(router)
app.mount("#app")
// createApp(App).mount('#app')
