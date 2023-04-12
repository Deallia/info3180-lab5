<template>
<h1>Upload Form </h1>
        <ul class="flash-messages">
            <li v-for="m in messages">
                 <div v-if="validated=='danger'" class="alert alert-danger">{{ m }}</div> 
             </li>
        </ul>
        <div v-if = "validated=='success'"  class="alert alert-success">{{messages.message }}</div>
    <form id = "movieForm" method="post"  enctype="multipart/form-data" @submit.prevent="saveMovie">
  
        <div class="form-group mb-3">
            <label for="title" class="form-label"> Movie Title </label>
            <input type="text" name="title" class="form-control" />
        </div>

        <div class="form-group mb-3">
            <label for="description" class="form-label"> Movie Description </label>
            <input type="text" name="description" class="form-control" />
        </div>

        <div class="form-group mb-3">
            <label for="poster"> Upload Poster</label>
            <input type="file"  name="poster" class ="form-control" />
        </div>
        <button class="btn btn-lg btn-primary w-100 mt-3" type="submit">Submit</button>
    </form>
    
</template>
<style>
    .flash-messages{
        list-style: none;
        margin-left: -10px;
        margin-right: 30px;
    }
    form,h1{
        margin:30px;
    }
</style>

<script setup>

import { ref, onMounted } from "vue";

let messages = ref([]);
let validated = ref("");
let csrf_token = ref("");

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
 }


function saveMovie (){

        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);

        fetch("/api/v1/movies", {
            method: 'POST',
            body: form_data,
            headers: {
                        'X-CSRFToken': csrf_token.value
                    }
            })
              .then(function(response) {
                  return response.json();
              })
              .then(function (data) {
                  // display a success message
                   console.log(data);

                   if(data.hasOwnProperty('errors')){
                    messages.value = data.errors;
                    validated.value = "danger";
                }   
                else{
                    messages.value = data;
                    validated.value = "success";
                }  
               })
              .catch(function (error) {
                   console.log(error);
               });
    }

onMounted(() => {
    getCsrfToken();
});
</script>