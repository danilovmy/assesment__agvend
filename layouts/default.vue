<template>
    <div>
      <header>Page Header</header>
      <slot /> <!-- This is where your page content will be rendered -->
      <footer>Page Footer</footer>
    </div>
</template>

<script>
export default {
  name: 'DefaultLayout'
}
</script>
