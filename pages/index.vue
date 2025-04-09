<template>
    <section>
        <h1>
            {{ title }}
        </h1>
        <div>
            <SearchString @change="sortData" />
            <div v-for="product in data" :key="product.id">
                <p>
                    <span>{{ product.id }}</span>
                    &nbsp;
                    <span>{{ product.name }}</span>
                </p>
            </div>
        </div>
    </section>
</template>


<script type="text/javascript">

export default {
    layout: 'default',
    async setup () {
        const { data } = await useFetch('/api/dataset')
        return { data }
    },
    data () {
        return{
            defaultData: this.data,
            title: "Assesment"
        }
    },
    methods: {
        sortData (text) {
            if (text && text.length > 2) {
                this.data = this.defaultData.filter(obj => obj.name.toLowerCase().includes(text) )
            } else {
                this.data = this.defaultData
            }
        }
    }
}
</script>