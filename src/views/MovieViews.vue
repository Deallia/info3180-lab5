<template>
  <h1 id="p-heading">Movies</h1>
    
    
      <ul class="img-grid">
        
        <li v-for="movie in movies" :key="movie.id">

          <div class="movie-card">
            <img :src= "movie.poster"  alt="Movie poster" width="100px" height="150px">
            <div class="details">
              <h3>{{ movie.title }}</h3>
              <p>{{ movie.description }}</p>
            </div>
        </div>
        </li>
      </ul>
    
  </template>

  
  
<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);



function fetchmovies(){
   
        fetch("/api/v1/movies", {
          method:'GET'
        })
              .then((response) => response.json())
              .then((data) => {
                       movies.value = data.Movies;
                      console.log(movies.value);
              })
              .catch(function (error) {
                   console.log(error);
               });
}

onMounted(() => {
  fetchmovies();
});
</script>

<style>
  .img-grid{
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  row-gap: 40px;
  flex-wrap:wrap;
  list-style: none;
  } 
  .movie-card{
    width:400px; 
    display: flex;
    flex-direction: row;
    box-shadow: 5px 6px 8px -7px #a5a8ac;  
    padding: 30px;

  }
  h1{
    margin-left: 65px;
  }
</style>