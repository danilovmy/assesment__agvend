// @ts-check
import withNuxt from './.nuxt/eslint.config.mjs'

export default withNuxt(
{
    root: true,
    env: {
        browser: true,
        node: true
    },
    parserOptions: {
        parser: '@babel/eslint-parser',
        requireConfigFile: false
    },
    extends: [
        '@nuxtjs',
        'plugin:nuxt/recommended'
    ],
    plugins: [],
    // add your custom rules here
    rules: {
        'nuxt/no-timing-in-fetch-data': 'off',
        indent: ['error', 4],
        'vue/script-indent': ['error', 4],
        'vue/max-attributes-per-line': ['error', { singleline: { max: 6 }, multiline: { max: 1 } }],
        'vue/html-indent': ['error', 4],
        'vue/html-self-closing': ['error', { html: { void: 'always', normal: 'never', component: 'always' }, svg: 'always', math: 'always' }]
    }
}
)
