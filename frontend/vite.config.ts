import {fileURLToPath, URL} from 'node:url'

import {defineConfig, searchForWorkspaceRoot} from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
    server: {
        fs: {
            allow: [
                // search up for workspace root
                searchForWorkspaceRoot(process.cwd()),
                // custom rules
                '/home/filippo/node_modules/primeicons/fonts/'
            ],
        },
    },
    plugins: [
        vue(),
        vueJsx(),
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }
})
