import { createStore } from 'vuex'

export const store = createStore({
    state() {
        return {
            api_url: import.meta.env.VITE_API_URL,
        }
    },
})