import { fileURLToPath, URL } from 'node:url'
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

export default ({ mode }) => {
  const env = loadEnv(mode, '/app') // en Docker, le dossier projet = /app

  return defineConfig({
    plugins: [vue()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: ''
        }
      }
    },
    server: {
      host: true,
      port: 5173,
      watch: {
        usePolling: true
      }
    },
    define: {
      'import.meta.env': Object.fromEntries(
        Object.entries(env).map(([key, val]) => [key, JSON.stringify(val)])
      )
    }
  })
}