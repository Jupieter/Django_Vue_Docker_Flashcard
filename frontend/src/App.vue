<template>
  <!DOCTYPE html>
  <html lang="en">

  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  </head>

  <body>
    <div id="app">
      <font-awesome-icon icon="user-secret" />
      <AppHeader />
      <CardSets />
    </div>
  </body>

  </html>
</template>


<script>
import CardSets from "./components/CardSets.vue";
import AppHeader from "./components/AppHeader.vue";
export default {
  name: "App",
  components: {
    AppHeader,
    CardSets,
  },
};
</script>


<style>
  .df {
    display: flex;
    gap: 1rem;
  }

</style>