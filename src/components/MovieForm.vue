<template>
    <h1>HELLO WORLD</h1>
    <form id = "movieForm" method="post"  enctype="multipart/form-data" @submit.prevent="saveMovie">
        {{ form.csrf_token }}
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title </label>
            <input type="text" name="title" class="form-control" />
        </div>

        <div class="form-group mb-3">
            <label for="description" class="form-label">Movie Description </label>
            <input type="text" name="description" class="form-control" />
        </div>

        <div class="form-group mb-3">
            <label for="poster">Upload Poster</label>
            <input type="file"  name="poster" class ="form-control" />
        </div>
        <button class="btn btn-lg btn-primary w-100 mt-3" type="submit">Submit</button>
    </form>
    
</template>


<script setup>

import { ref, onMounted } from "vue";

let csrf_token = ref("");

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
 }

onMounted(() => {
    getCsrfToken();
});


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
            .then(function (response) {
                return response.json();
                })
            .then(function (data) {
                // display a success message
                console.log(data);
                })
            .catch(function (error) {
                console.log(error);
                });
    }
</script>