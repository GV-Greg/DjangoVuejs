import { defineStore } from 'pinia'
import http from '@/services/api'

export const useConfigStore = defineStore('config', {
    state: () => ({
        fusion: false
    }),
    getters: {
        getFusion: (state) => state.fusion,
        
    },
    actions: {
        setFusion(fusion) {
            this.fusion = fusion
        },
        async initialize() {
            await http.get()
        }

    }
})