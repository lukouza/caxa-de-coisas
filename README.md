rm vite.config.js
printf "import { defineConfig } from 'vite';\nimport laravel from 'laravel-vite-plugin';\n\nexport default defineConfig({\n    plugins: [\n        laravel({\n            input: ['resources/css/app.css', 'resources/js/app.js'],\n            refresh: true,\n        }),\n    ],\n});\n" > vite.config.js
