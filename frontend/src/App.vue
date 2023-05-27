<template>
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    </head>
    
    <body>
      <div id="app">
        <TasksItem />
      </div>
    </body>
  </html>
</template>


<script>
import TasksItem from "./components/TasksItem.vue";
export default {
  name: "App",
  components: {
    TasksItem,
  },
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.selector-for-some-widget {
  box-sizing: content-box;
}
</style>