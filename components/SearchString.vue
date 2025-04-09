<template>
    <input type="search" @keyup="changeinput">
</template>

<script>

export default {
    emits: ['change'],
    methods: {
        changeinput (event) {
            this.$emit('change', event.target.value.toLowerCase())
         }
    }
}
</script>